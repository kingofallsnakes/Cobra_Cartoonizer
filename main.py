import cv2
import os
import numpy as np
from tkinter import Tk, Label, Button, filedialog, StringVar, OptionMenu, Frame, messagebox, Canvas
from PIL import Image, ImageTk

class Cartoonizer:
    def __init__(self, down_samples=2, bilateral_filters=50):
        self.down_samples = down_samples
        self.bilateral_filters = bilateral_filters

    def render(self, img_rgb):
        img_rgb = cv2.resize(img_rgb, (1366, 768))
        img_color = img_rgb.copy()
        for _ in range(self.down_samples):
            img_color = cv2.pyrDown(img_color)
        for _ in range(self.bilateral_filters):
            img_color = cv2.bilateralFilter(img_color, 9, 9, 7)
        for _ in range(self.down_samples):
            img_color = cv2.pyrUp(img_color)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
        img_blur = cv2.medianBlur(img_gray, 3)
        img_edge = cv2.adaptiveThreshold(img_blur, 255,
                                          cv2.ADAPTIVE_THRESH_MEAN_C,
                                          cv2.THRESH_BINARY, 9, 2)
        img_edge = cv2.cvtColor(cv2.resize(img_edge, (img_color.shape[1], img_color.shape[0])),
                                 cv2.COLOR_GRAY2RGB)
        return cv2.bitwise_and(img_color, img_edge)

class App:
    def __init__(self, root):
        self.cartoonizer = Cartoonizer()
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Cobra Cartoonizer")
        self.root.geometry("1000x800")
        self.root.configure(bg="#282c34")
        self.frame = Frame(self.root, bg="#444b55", bd=2, relief="groove")
        self.frame.pack(pady=10, padx=10, fill="both")
        self.create_ui_elements()
        self.layout_ui_elements()

    def create_ui_elements(self):
        self.label = Label(self.frame, text="Select an image to cartoonify:", font=("Helvetica", 16, "bold"),
                           fg="#ffffff", bg="#444b55", anchor="w")
        self.instructions_label = Label(self.frame, text="Choose a filter and adjust settings before applying.",
                                         font=("Helvetica", 12), fg="#ffffff", bg="#444b55", anchor="w")
        self.select_button = Button(self.frame, text="Select Image", command=self.select_image,
                                    bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"), width=12)
        self.process_button = Button(self.frame, text="Apply Filter", command=self.apply_filter,
                                     bg="#2196F3", fg="white", font=("Helvetica", 12, "bold"), width=12)
        self.reset_button = Button(self.frame, text="Reset", command=self.reset,
                                   bg="#f44336", fg="white", font=("Helvetica", 12, "bold"), width=12)
        self.save_button = Button(self.frame, text="Save", command=self.save_image,
                                  bg="#FFC107", fg="black", font=("Helvetica", 12, "bold"), width=12)
        self.status_label = Label(self.root, text="", fg="blue", bg="#282c34", font=("Helvetica", 12))
        self.preview_canvas = Canvas(self.root, width=700, height=450, bg="white", bd=2, relief="ridge")

    def layout_ui_elements(self):
        self.label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.instructions_label.grid(row=0, column=1, sticky="w", padx=10, pady=10)
        self.select_button.grid(row=1, column=0, padx=10, pady=(10, 0))
        self.filter_var = StringVar(self.root)
        self.filter_var.set("Cartoon")
        self.filters = ["Cartoon", "Sketch", "Pencil", "Color Filter", "Grayscale", "Blur", "Edge Detection",
                        "Sepia", "Negative", "Emboss"]
        self.filter_menu = OptionMenu(self.frame, self.filter_var, *self.filters)
        self.filter_menu.config(bg="#2196F3", fg="white", font=("Helvetica", 12, "bold"), width=12)
        self.filter_menu.grid(row=1, column=1, padx=10, pady=(10, 0))
        self.process_button.grid(row=2, column=0, padx=10)
        self.reset_button.grid(row=2, column=1, padx=10)
        self.save_button.grid(row=3, column=0, padx=10)
        self.status_label.pack(pady=10)
        self.preview_canvas.pack(pady=10)

    def select_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if self.image_path:
            self.status_label.config(text=f"Selected: {self.image_path}")
            self.display_image(cv2.imread(self.image_path))

    def display_image(self, image):
        try:
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image_resized = self.resize_image(image_rgb)
            self.preview_image = Image.fromarray(image_resized)
            self.preview_image_tk = ImageTk.PhotoImage(self.preview_image)
            self.preview_canvas.create_image(0, 0, anchor="nw", image=self.preview_image_tk)
            self.preview_canvas.image = self.preview_image_tk
        except Exception as e:
            messagebox.showerror("Display Error", f"Could not display the image. Error: {e}")

    def resize_image(self, image):
        max_size = 750
        h, w, _ = image.shape
        if h > w:
            new_h = max_size
            new_w = int(max_size * (w / h))
        else:
            new_w = max_size
            new_h = int(max_size * (h / w))
        return cv2.resize(image, (new_w, new_h))

    def apply_filter(self):
        if not getattr(self, 'image_path', None):
            messagebox.showwarning("No Image", "Please select an image first.")
            return
        try:
            img_rgb = cv2.imread(self.image_path)
            filtered_img = self.cartoonizer.render(img_rgb)
            selected_filter = self.filter_var.get()
            filtered_img = self.apply_selected_filter(filtered_img, selected_filter)
            self.display_image(filtered_img)
            self.status_label.config(text="Filter applied successfully!")
        except Exception as e:
            messagebox.showerror("Processing Error", f"Could not apply the filter. Error: {e}")

    def apply_selected_filter(self, image, filter_name):
        filters_map = {
            "Sketch": lambda img: cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
            "Pencil": lambda img: cv2.Canny(img, 100, 200),
            "Color Filter": lambda img: cv2.applyColorMap(img, cv2.COLORMAP_JET),
            "Grayscale": lambda img: cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
            "Blur": lambda img: cv2.GaussianBlur(img, (15, 15), 0),
            "Edge Detection": lambda img: cv2.Canny(img, 100, 200),
            "Sepia": lambda img: cv2.transform(img, np.array([[0.272, 0.534, 0.131],
                                                               [0.349, 0.686, 0.168],
                                                               [0.393, 0.769, 0.189]])),
            "Negative": lambda img: cv2.bitwise_not(img),
            "Emboss": lambda img: cv2.filter2D(img, -1, np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]))
        }
        return filters_map.get(filter_name, lambda img: img)(image)

    def save_image(self):
        if not getattr(self, 'image_path', None):
            messagebox.showwarning("No Image", "Please select an image first.")
            return

        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), 
                                                                                   ("JPEG files", "*.jpg")])
        if save_path:
            cv2.imwrite(save_path, cv2.cvtColor(np.array(self.preview_image), cv2.COLOR_RGB2BGR))
            messagebox.showinfo("Save Successful", f"Image saved to: {save_path}")

    def reset(self):
        self.image_path = None
        self.preview_canvas.delete("all")
        self.status_label.config(text="Select an image to start.")
        self.filter_var.set("Cartoon")

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
