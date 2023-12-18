import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


def change_image_position():
    image_label.configure(compound=f"{image_position.get()}")


def change_image_to_top():
    image_position.set("top")
    change_image_position()


def change_image_to_bottom():
    image_position.set("bottom")
    change_image_position()


# root configurations
root = tk.Tk()
root.geometry("600x450")
root.title("Labels workout")
root.resizable(False, False)

# Text label configuration
text_label = ttk.Label(root, text="Working with Labels", padding=20)
text_label.configure(font=("Seago UI", 20))
text_label.pack()

# Image label configurations
image = Image.open("./images/sunrise.jpg").resize((500, 300))
photo = ImageTk.PhotoImage(image)
image_label = ttk.Label(
    root, image=photo, text="Beautiful Sunrise", compound="top"
)
image_label.config(font=("areial black", 15))
image_label.pack()

# Buttons configurations
buttons_frame = ttk.Frame(root)
buttons_frame.pack(pady=(10, 10))
image_position = tk.StringVar()

top_button = ttk.Button(
    buttons_frame, text="Bottom Text", command=change_image_to_top
)
top_button.pack(side="left", padx=(0, 10))

bottom_button = ttk.Button(
    buttons_frame, text="Top Text", command=change_image_to_bottom
)
bottom_button.pack(side="left")


root.mainloop()
