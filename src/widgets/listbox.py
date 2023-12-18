import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("ListBox workout")

mobile_options = ("Realme", "Redmi", "Poco", "Samsung", "OnePlus")
mobiles = tk.StringVar(value=mobile_options)

listbox = tk.Listbox(root, listvariable=mobiles, height=4)
listbox["selectmode"] = "extended"  # browse
listbox.pack()


def handle_selection(event):
    selected_indices = listbox.curselection()
    for index in selected_indices:
        print(listbox.get(index))


listbox.bind("<<ListboxSelect>>", handle_selection)

root.mainloop()
