from tkinter import ttk
import tkinter as tk


class SendMessage(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.container = container
        self.add_send_box()
        self.add_buttons()

    def add_send_box(self):
        self.message_box = tk.Text(self, height=5)
        self.message_box.grid(row=0, column=0, sticky="EW", padx=(0, 15))

    def add_buttons(self):
        buttons_frame = ttk.Frame(self)
        send_button = ttk.Button(
            buttons_frame,
            text="Send",
            command=self.container.handle_send_message,
            style="SendButton.TButton",
        )
        fetch_button = ttk.Button(
            buttons_frame,
            text="Fetch",
            command=self.container.handle_message_display,
        )
        send_button.pack(pady=(0, 5))
        fetch_button.pack()
        buttons_frame.grid(row=0, column=1, padx=(0, 5))
