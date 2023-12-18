import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class DisplayMessages(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.main_canvas = tk.Canvas(self)
        self.main_frame = ttk.Frame(self.main_canvas, style="Messages.TFrame")
        self.add_scroll_bar()

    def add_messages(self, messages):
        for message in messages:
            message_frame = ttk.Frame(self.main_frame)
            avatar_image = Image.open("./images/male.jpg").resize((50, 50))
            avatar_photo = ImageTk.PhotoImage(avatar_image)
            avatar_label = ttk.Label(
                message_frame, image=avatar_photo, style="Avatar.TLabel"
            )
            avatar_label.image = avatar_photo
            date_label = ttk.Label(
                message_frame, text=message["date"], style="Time.TLabel"
            )
            message_label = ttk.Label(
                message_frame, text=message["message"], style="Message.TLabel"
            )
            avatar_label.grid(row=0, column=0, rowspan=2)
            date_label.grid(row=0, column=1, sticky="EW")
            message_label.grid(row=1, column=1, sticky="EW")
            message_frame.pack(fill="x", pady=(0, 5))

    def add_scroll_bar(self):
        scroll_bar = ttk.Scrollbar(self)
        scroll_bar.configure(command=self.main_canvas.yview)
        self.main_canvas.config(yscrollcommand=scroll_bar.set)
        scroll_bar.pack(side="right", fill="y")
        self.main_canvas.pack(side="left", fill="both", expand=True)
        self.main_canvas.create_window(
            (0, 0), anchor="nw", window=self.main_frame
        )
        self.main_frame.bind(
            "<Configure>",
            lambda event: self.main_canvas.configure(
                scrollregion=self.main_canvas.bbox("all"),
            ),
        )
