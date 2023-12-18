import tkinter as tk
from tkinter import ttk


def greet():
    print("Welcome")


root = tk.Tk()
root.title("First App")

ttk.Label(root, text="Hello world!", padding=(80, 20)).pack()

greet_button = ttk.Button(root, text="Greet", command=greet)
greet_button.pack(side="left")
quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(fill="x")

root.mainloop()
