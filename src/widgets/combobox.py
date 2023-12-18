import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("ComboBox workout")

selected_month = tk.StringVar()

month_selector = ttk.Combobox(root, textvariable=selected_month)
month_selector["value"] = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
)
month_selector.pack()
month_selector["state"] = "readonly"


def handle_selection(event):
    print(f"Selected month from variable {selected_month.get()}")
    print(f"Selected month from selector {month_selector.get()}")
    print(
        f"Selected month's current from selector {month_selector.current()}"
    )


month_selector.bind("<<ComboboxSelected>>", handle_selection)

root.mainloop()
