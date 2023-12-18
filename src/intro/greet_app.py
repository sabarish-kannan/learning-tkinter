import tkinter as tk
from tkinter import ttk


def greet():
    print(f"Hello {user_name.get() or 'world!'}")


root = tk.Tk()

input_frame = ttk.Frame(root)
input_frame.pack(pady=(20, 10))

user_name = tk.StringVar()
name_label = ttk.Label(input_frame, text="Name:")
name_label.pack(side="left", padx=(0, 10))
name_entry = ttk.Entry(input_frame, textvariable=user_name)
name_entry.focus()
name_entry.pack(side="left")


buttons_frame = ttk.Frame(root)
buttons_frame.pack(padx=(10, 10), fill="x")

greet_button = ttk.Button(buttons_frame, text="Greet", command=greet)
greet_button.pack(side="left", padx=(0, 10), expand=True, fill="x")

quit_button = ttk.Button(buttons_frame, text="Quit", command=root.destroy)
quit_button.pack(side="left", expand=True, fill="x")


root.mainloop()
