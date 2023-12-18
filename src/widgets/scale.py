import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Scale workout")


def handle_scale(event):
    print(scale.get())


variable = tk.DoubleVar()
scale = ttk.Scale(
    root, variable=variable, from_=0, to=10, command=handle_scale
)
scale.pack(fill="x", padx=20)


root.mainloop()
