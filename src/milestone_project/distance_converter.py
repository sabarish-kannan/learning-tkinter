import tkinter as tk
import tkinter.font as font
from tkinter import ttk

root = tk.Tk()
root.title("Distance Converter")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

font.nametofont("TkDefaultFont").configure(size=20)


def meter_to_feet(*args):
    try:
        feet = float(meter_value.get()) * 3.28084
        feet_value.set(f"{feet}")
    except:
        print("Enter only numbers for meter")


main = ttk.Frame(root)
main.grid(padx=10, pady=10)

meter_value = tk.StringVar()
feet_value = tk.StringVar(value="Feet will display here")

meter_label = ttk.Label(main, text="Meter:")
meter_entry = ttk.Entry(
    main, width=10, textvariable=meter_value, font=("Arial black", 20)
)
meter_entry.focus()
feet_label = ttk.Label(main, text="Feet:")
feet_result = ttk.Label(main, textvariable=feet_value)
calculate_button = ttk.Button(main, text="Calculate", command=meter_to_feet)

meter_label.grid(column=0, row=0, sticky="W")
meter_entry.grid(column=1, row=0, sticky="EW")
feet_label.grid(column=0, row=1, sticky="W")
feet_result.grid(column=1, row=1, sticky="EW")
calculate_button.grid(column=0, row=2, columnspan=2, sticky="EW")

root.bind("<Return>", meter_to_feet)
root.bind("<KP_Enter>", meter_to_feet)

for child in main.winfo_children():
    child.grid_configure(padx=10, pady=10)

root.mainloop()
