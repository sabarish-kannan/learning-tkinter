import tkinter as tk
from tkinter import ttk


def greet():
    print(f"Hello {user_name.get() or 'world!'}")


root = tk.Tk()
root.columnconfigure(0, weight=1)

input_frame = ttk.Frame(root)
input_frame.grid(row=0, column=0, sticky="EW", padx=5, pady=5)

user_name = tk.StringVar()
name_label = ttk.Label(input_frame, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5)
input_field = ttk.Entry(input_frame, width=15, textvariable=user_name)
input_field.grid(row=0, column=1, padx=5, pady=5)

buttons_frame = ttk.Frame(root)
buttons_frame.grid(row=1, column=0, sticky="EW", padx=(10, 10))
buttons_frame.columnconfigure(0, weight=1)
buttons_frame.columnconfigure(1, weight=1)

greet_button = ttk.Button(buttons_frame, text="Greet", command=greet)
greet_button.grid(row=0, column=0, sticky="EW", padx=5, pady=5)
quit_button = ttk.Button(buttons_frame, text="Quit", command=root.destroy)
quit_button.grid(row=0, column=1, sticky="EW", padx=5, pady=5)


style = ttk.Style(root)
print(style.theme_names())
print(style.theme_use())  # Get the current theme name
style.theme_use("clam")
print(name_label.winfo_class())  # To get the applied style for the widget
style.configure("TLabel", font=("Segoe UI", 13))


root.mainloop()
