import tkinter as tk
from tkinter import ttk


class UserInputFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.user_name = tk.StringVar()
        self.user_name_label = ttk.Label(self, text="Enter user name: ")
        self.user_name_entry = ttk.Entry(self, textvariable=self.user_name)
        self.submit = ttk.Button(self, text="Submit", command=self.greet)

        self.user_name_label.pack(side="left")
        self.user_name_entry.pack(side="left")
        self.submit.pack(side="left")

    def greet(self):
        print(f"Hello {self.user_name.get() or 'World!'}")


root = tk.Tk()
UserInputFrame(root).pack()


root.mainloop()
