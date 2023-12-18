import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("SpinBox workout")

input_value = tk.StringVar(value=0)
spinbox = ttk.Spinbox(
    root,
    textvariable=input_value,
    # from_=0,
    # to=20,
    values=(2, 4, 6, 8, 10, 12, 14, 16, 18, 20),
)
spinbox.pack()

print(spinbox.get())

root.mainloop()
