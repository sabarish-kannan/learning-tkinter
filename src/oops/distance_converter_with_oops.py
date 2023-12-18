import tkinter as tk
import tkinter.font as font
from tkinter import ttk


class DistanceConverter(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.title("Distance converter")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.frame = MeterToFeet(self, self.swap_converter)
        self.frame.grid(row=0, column=0, padx=10, pady=10)

        self.bind("<Return>", self.frame.convert)
        self.bind("<KP_Enter>", self.frame.convert)

        for child in self.frame.winfo_children():
            child.grid_configure(padx=10, pady=10)

    def swap_converter(self):
        if isinstance(self.frame, MeterToFeet):
            self.frame.destroy()
            self.frame = FeetToMeter(self, self.swap_converter)
        else:
            self.frame.destroy()
            self.frame = MeterToFeet(self, self.swap_converter)
        self.frame.grid(row=0, column=0, padx=10, pady=10)
        self.bind("<Return>", self.frame.convert)
        self.bind("<KP_Enter>", self.frame.convert)

        for child in self.frame.winfo_children():
            child.grid_configure(padx=10, pady=10)


class MeterToFeet(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)
        self.meter_value = tk.StringVar()
        self.feet_value = tk.StringVar(value="Feet will display here")

        meter_label = ttk.Label(self, text="Meter:")
        meter_entry = ttk.Entry(
            self,
            width=10,
            textvariable=self.meter_value,
            font=("Arial black", 20),
        )
        meter_entry.focus()
        feet_label = ttk.Label(self, text="Feet:")
        feet_result = ttk.Label(self, textvariable=self.feet_value)
        calculate_button = ttk.Button(
            self, text="Calculate", command=self.convert
        )
        switch_button = ttk.Button(
            self, text="Swap converters", command=controller
        )

        meter_label.grid(column=0, row=0, sticky="W")
        meter_entry.grid(column=1, row=0, sticky="EW")
        feet_label.grid(column=0, row=1, sticky="W")
        feet_result.grid(column=1, row=1, sticky="EW")
        calculate_button.grid(column=0, row=2, columnspan=2, sticky="EW")
        switch_button.grid(row=3, column=0, columnspan=2, sticky="EW")

    def convert(self, *args):
        try:
            feet = float(self.meter_value.get()) * 3.28084
            self.feet_value.set(f"{feet}")
        except:
            self.feet_value.set("Enter only numbers for meter")


class FeetToMeter(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)
        self.meter_value = tk.StringVar(value="Meter will display here")
        self.feet_value = tk.StringVar()

        feet_label = ttk.Label(self, text="Feet:")
        feet_entry = ttk.Entry(
            self,
            width=10,
            textvariable=self.feet_value,
            font=("Arial black", 20),
        )
        feet_entry.focus()
        meter_label = ttk.Label(self, text="Meter:")
        meter_result = ttk.Label(self, textvariable=self.meter_value)
        calculate_button = ttk.Button(
            self, text="Calculate", command=self.convert
        )
        switch_button = ttk.Button(
            self, text="Swap converters", command=controller
        )

        feet_label.grid(column=0, row=0, sticky="W")
        feet_entry.grid(column=1, row=0, sticky="EW")
        meter_label.grid(column=0, row=1, sticky="W")
        meter_result.grid(column=1, row=1, sticky="EW")
        calculate_button.grid(column=0, row=2, columnspan=2, sticky="EW")
        switch_button.grid(row=3, column=0, columnspan=2, sticky="EW")

    def convert(self, *args):
        try:
            meter = float(self.feet_value.get()) / 3.28084
            self.meter_value.set(f"{meter}")
        except:
            self.meter_value.set("Enter only numbers for meter")


root = DistanceConverter()

font.nametofont("TkDefaultFont").configure(size=15)

root.mainloop()
