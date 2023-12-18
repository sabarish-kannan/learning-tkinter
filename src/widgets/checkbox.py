import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("CheckBox workout")

check_value = tk.StringVar()


def print_check_value():
    print(check_value.get())


check_button = ttk.Checkbutton(
    root,
    text="Check me!",
    command=print_check_value,
    variable=check_value,
    onvalue="I am checked",
    offvalue="I am unchecked",
)
check_button.pack()

root.mainloop()
