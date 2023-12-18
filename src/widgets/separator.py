import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Separator workout")

ttk.Label(root, text="First Line").pack(pady=10)

ttk.Separator(root, orient="horizontal").pack(fill="x")

ttk.Label(root, text="Second Line").pack(pady=10)

root.mainloop()
