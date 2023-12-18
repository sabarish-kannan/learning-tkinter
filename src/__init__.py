import tkinter as tk
from tkinter import ttk

root = tk.Tk()

rectangle1 = ttk.Label(
    root,
    text="Rectangle 1",
    foreground="black",
    background="green",
)
rectangle1.pack(fill="both", expand=True)
rectangle2 = ttk.Label(
    root,
    text="Rectangle 2",
    foreground="black",
    background="red",
)
rectangle2.pack(side="left", fill="both", expand=True)
rectangle3 = ttk.Label(
    root,
    text="Rectangle 3",
    foreground="black",
    background="yellow",
)
rectangle3.pack(fill="both")

root.mainloop()
