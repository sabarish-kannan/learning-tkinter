import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Scrollbar workout")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame = ttk.Frame(root)
frame.grid(row=0, column=0, sticky="ew")
frame.columnconfigure(0, weight=1)

text = tk.Text(frame, height=10)
text.grid(row=0, column=0, sticky="ew")
text.insert("1.0", "Enter your Thoughts.")

scroll_bar = ttk.Scrollbar(frame, orient="vertical", command=text.yview)
scroll_bar.grid(row=0, column=1, sticky="ns")
text["yscrollcommand"] = scroll_bar.set

root.mainloop()
