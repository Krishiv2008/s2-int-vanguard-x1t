import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from PIL import Image, ImageTk
import os
import json

IMAGE_DIR = r'E:\vanguard_project\test\images'           # <-- Change this to your images folder path
ANNOTATION_DIR = 'annotations'
os.makedirs(ANNOTATION_DIR, exist_ok=True)

# COCO categories you want (edit as needed)
CLASSES = [
    'military_tank',
    'military_person',
    'armored_carrier',
    'air_fighter',
    'bomber',
]

CATEGORY_ID = {name: idx+1 for idx, name in enumerate(CLASSES)}

class AnnotatorApp:
    def __init__(self, master):
        self.root = master
        self.root.title("COCO Annotator")
        self.canvas = tk.Canvas(master, cursor="cross")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Controls
        control = tk.Frame(master)
        control.pack(side=tk.RIGHT, fill=tk.Y)

        tk.Label(control, text="Class Label:").pack()
        self.class_var = tk.StringVar(value=CLASSES[0])
        self.class_dropdown = ttk.Combobox(control, textvariable=self.class_var, values=CLASSES)
        self.class_dropdown.pack()

        tk.Button(control, text="Open Images", command=self.open_images).pack(pady=10)
        tk.Button(control, text="Prev", command=lambda: self.switch_image(-1)).pack()
        tk.Button(control, text="Next", command=lambda: self.switch_image(1)).pack()
        tk.Button(control, text="Save to COCO JSON", command=self.save_annotations).pack(pady=10)

        self.mode_box = tk.Button(control, text="Mode: Box", command=self.toggle_mode)
        self.mode_box.pack(pady=5)
        self.mode = "box"

        self.info_label = tk.Label(control, text="Draw box: click-drag\nPolygon: click points, Right click to finish")
        self.info_label.pack()

        self.reset_btn = tk.Button(control, text="Clear this image", command=self.clear_image_annotations)
        self.reset_btn.pack(pady=5)

        # Data
        self.image_paths = []
        self.cur_image_index = 0
        self.cur_image = None
        self.tk_im = None
        self.img_id_map = {}
        self.polypoints = []  # For polygons
        self.cur_shape_id = None

        # All annotations (COCO format)
        self.coco = {
            "images": [],
            "annotations": [],
            "categories": [ {"id": i+1, "name": n} for i, n in enumerate(CLASSES) ]
        }
        self.ann_id = 1

        # Per-image session cache
        self.img_anns = {}

        # Canvas mouse handlers
        self.drawing = False
        self.bbox_start = None
        self.canvas.bind("<Button-1>", self.mouse_down)
        self.canvas.bind("<B1-Motion>", self.mouse_move)
        self.canvas.bind("<ButtonRelease-1>", self.mouse_up)
        self.canvas.bind("<Button-3>", self.finish_polygon)  # right click

    ### -- Image Handling ---

    def open_images(self):
        self.image_paths = filedialog.askopenfilenames(title="Select Images", 
                                                       filetypes=[("Image files", "*.jpg *.jpeg *.png")],
                                                       initialdir=IMAGE_DIR)
        if not self.image_paths:
            return
        self.cur_image_index = 0
        self.load_image()

    def switch_image(self, delta):
        if not self.image_paths:
            return
        new_index = self.cur_image_index + delta
        if 0 <= new_index < len(self.image_paths):
            self.cur_image_index = new_index
            self.polypoints = []  # clear unfinished polygons
            self.load_image()
        else:
            messagebox.showinfo("Info", "No more images in this direction.")

    def load_image(self):
        self.canvas.delete("all")
        if not self.image_paths:
            return
        img_path = self.image_paths[self.cur_image_index]
        self.cur_image = Image.open(img_path)
        self.tk_im = ImageTk.PhotoImage(self.cur_image)
        # Resize canvas to image size
        self.canvas.config(width=self.tk_im.width(), height=self.tk_im.height())
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_im)
        self.root.title(f"COCO Annotator - {os.path.basename(img_path)}")
        self.polypoints = []
        self.cur_shape_id = None

        # Load annotations for this image (if any)
        self.load_single_img_ann(img_path)
        # Redraw boxes/polygons
        self.redraw_annotations()

    ### -- Drawing ---

    def toggle_mode(self):
        if self.mode == "box":
            self.mode = "polygon"
            self.mode_box.configure(text="Mode: Polygon")
            self.info_label.config(text="Polygon: left click pts, right click to finish")
        else:
            self.mode = "box"
            self.mode_box.configure(text="Mode: Box")
            self.info_label.config(text="Draw box: click-drag")

    def mouse_down(self, event):
        if not self.cur_image: return
        if self.mode == "box":
            self.drawing = True
            self.bbox_start = (event.x, event.y)
        else:
            # Polygon mode
            self.polypoints.append((event.x, event.y))
            # Draw temp point
            r = 3
            self.canvas.create_oval(event.x-r, event.y-r, event.x+r, event.y+r, fill="blue", outline="blue", tags="polygon")
            np = len(self.polypoints)
            if np > 1:
                self.canvas.create_line(*self.polypoints[-2], *self.polypoints[-1], fill="blue", width=2, tags="polygon")

    def mouse_move(self, event):
        if self.drawing and self.mode == "box":
            if self.cur_shape_id:
                self.canvas.delete(self.cur_shape_id)
            x0, y0 = self.bbox_start
            x1, y1 = event.x, event.y
            self.cur_shape_id = self.canvas.create_rectangle(x0, y0, x1, y1, outline="red", width=2, dash=(2,2))

    def mouse_up(self, event):
        if self.drawing and self.mode == "box":
            x0, y0 = self.bbox_start
            x1, y1 = event.x, event.y
            box = (min(x0,x1), min(y0,y1), abs(x1-x0), abs(y1-y0))
            label = self.class_var.get()
            self.add_box_annotation(box, label)
            self.drawing = False
            if self.cur_shape_id:
                self.canvas.delete(self.cur_shape_id)
                self.cur_shape_id = None

    def finish_polygon(self, event):
        # End polygon and add annotation
        if self.mode != "polygon" or not self.polypoints: return
        # Draw closing line
        if len(self.polypoints) > 2:
            self.canvas.create_line(*self.polypoints[-1], *self.polypoints[0], fill="blue", width=2, tags="polygon")
            label = self.class_var.get()
            seg = [ [c for xy in self.polypoints for c in xy] ]  # COCO format: list of list
            self.add_poly_annotation(seg, label)
        self.polypoints = []
        self.canvas.delete("polygon")

    def add_box_annotation(self, bbox, label):
        img_path = self.image_paths[self.cur_image_index]
        img_id = self.get_image_id(img_path)
        ann = {
            "id": self.ann_id,
            "image_id": img_id,
            "category_id": CATEGORY_ID[label],
            "bbox": list(map(float, bbox)),  # [x, y, width, height]
            "segmentation": [],
            "area": float(bbox[2]*bbox[3]),
            "iscrowd": 0,
        }
        self.append_annotation(img_path, ann)
        self.draw_rectangle(bbox, label)
        self.ann_id += 1
        self.save_single_img_ann(img_path)  # Autosave

    def add_poly_annotation(self, segmentation, label):
        img_path = self.image_paths[self.cur_image_index]
        img_id = self.get_image_id(img_path)
        xs, ys = zip(*self.polypoints)
        xmin, xmax = min(xs), max(xs)
        ymin, ymax = min(ys), max(ys)
        bbox = [float(xmin), float(ymin), float(xmax-xmin), float(ymax-ymin)]
        ann = {
            "id": self.ann_id,
            "image_id": img_id,
            "category_id": CATEGORY_ID[label],
            "bbox": bbox,
            "segmentation": segmentation,
            "area": float(bbox[2]*bbox[3]),  # polygon area calculation optional
            "iscrowd": 0,
        }
        self.append_annotation(img_path, ann)
        self.draw_polygon(self.polypoints, label)
        self.ann_id += 1
        self.save_single_img_ann(img_path)  # Autosave

    def draw_rectangle(self, bbox, label=None):
        x, y, w, h = bbox
        shape = self.canvas.create_rectangle(x, y, x+w, y+h, outline="green", width=2)
        self.canvas.create_text(x+5, y+5, anchor="nw", text=label, fill="yellow", font=("TkDefaultFont",8,'bold'))

    def draw_polygon(self, pts, label=None):
        flat = [c for xy in pts for c in xy]
        shape = self.canvas.create_polygon(flat, outline="green", fill="", width=2)
        x, y = pts[0]
        self.canvas.create_text(x, y, anchor="nw", text=label, fill="yellow", font=("TkDefaultFont",8,'bold'))

    ### -- Annotation Storage and Loading ---

    def get_image_id(self, img_path):
        # Ensures consistent image ids for COCO
        if img_path not in self.img_id_map:
            self.img_id_map[img_path] = len(self.img_id_map) + 1
        return self.img_id_map[img_path]

    def append_annotation(self, img_path, ann):
        self.img_anns.setdefault(img_path, []).append(ann)

    def load_single_img_ann(self, img_path):
        base = os.path.splitext(os.path.basename(img_path))[0]
        ann_path = os.path.join(ANNOTATION_DIR, base+'.json')
        self.img_anns[img_path] = []
        if os.path.exists(ann_path):
            try:
                with open(ann_path, 'r') as f:
                    anns = json.load(f)
                for ann in anns:
                    self.append_annotation(img_path, ann)
                self.ann_id = max([a["id"] for a in anns]+[self.ann_id])
            except Exception as e:
                messagebox.showwarning("Warning", f"Failed to load annotations for {base}:\n{e}")

    def save_single_img_ann(self, img_path):
        # Only those for this image
        anns = self.img_anns.get(img_path, [])
        if not anns:
            return
        base = os.path.splitext(os.path.basename(img_path))[0]
        ann_path = os.path.join(ANNOTATION_DIR, base+'.json')
        with open(ann_path, 'w') as f:
            json.dump(anns, f, indent=2)

    def redraw_annotations(self):
        img_path = self.image_paths[self.cur_image_index]
        anns = self.img_anns.get(img_path, [])
        for ann in anns:
            if ann['segmentation']:
                pts = [(ann['segmentation'][0][i], ann['segmentation'][0][i+1]) for i in range(0, len(ann['segmentation'][0]), 2)]
                self.draw_polygon(pts, self.get_labelname(ann['category_id']))
            else:
                self.draw_rectangle(ann['bbox'], self.get_labelname(ann['category_id']))

    def get_labelname(self, category_id):
        for k, v in CATEGORY_ID.items():
            if v == category_id: return k
        return str(category_id)

    def clear_image_annotations(self):
        img_path = self.image_paths[self.cur_image_index]
        self.img_anns[img_path] = []
        self.canvas.delete("all")
        self.canvas.create_image(0,0,anchor=tk.NW, image=self.tk_im)
        self.save_single_img_ann(img_path)

    def save_annotations(self):
        # Compile global COCO json from per-img sessions
        images = []
        annotations = []
        for img_path in self.image_paths:
            img = Image.open(img_path)
            base = os.path.splitext(os.path.basename(img_path))[0]
            img_id = self.get_image_id(img_path)
            images.append({
                "id": img_id,
                "file_name": os.path.basename(img_path),
                "height": img.height,
                "width": img.width,
            })
            anns = self.img_anns.get(img_path, [])
            for ann in anns:
                annotations.append(ann)
        self.coco["images"] = images
        self.coco["annotations"] = annotations
        with open(os.path.join(ANNOTATION_DIR,"coco_annotations.json"),'w') as f:
            json.dump(self.coco, f, indent=2)
        messagebox.showinfo("Saved", "All annotations exported in COCO format.")

# --- Run ---

if __name__ == "__main__":
    root = tk.Tk()
    app = AnnotatorApp(root)
    root.mainloop()
