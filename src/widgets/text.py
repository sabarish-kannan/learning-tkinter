import tkinter as tk
from tkinter import ttk


def print_input():
    text_content = text.get("1.0", "end")
    print(text_content)


root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Text workout")

text = tk.Text(root, height=10)
text.pack()
text.insert("1.0", "Enter your Thoughts.")
text["state"] = "normal"  # disable

submit = ttk.Button(root, text="Submit Thoughts", command=print_input)
submit.pack(pady=(20, 0))

root.mainloop()
