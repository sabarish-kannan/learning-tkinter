import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("RadioButton workout")

selected_option = tk.StringVar()

option_1 = ttk.Radiobutton(
    root, text="Option 1", variable=selected_option, value="selected option 1"
)
option_2 = ttk.Radiobutton(
    root, text="Option 2", variable=selected_option, value="selected option 2"
)
option_3 = ttk.Radiobutton(
    root, text="Option 3", variable=selected_option, value="selected option 3"
)

option_1.pack()
option_2.pack()
option_3.pack()

root.mainloop()
