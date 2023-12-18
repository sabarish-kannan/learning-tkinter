from datetime import datetime
import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from handle_messages import HandleMessages
from frames.message_display_frame import DisplayMessages
from frames.message_sending_frame import SendMessage

COLOUR_LIGHT_BACKGROUND_1 = "#fff"
COLOUR_LIGHT_BACKGROUND_2 = "#f2f3f5"
COLOUR_LIGHT_BACKGROUND_3 = "#e3e5e8"

COLOUR_LIGHT_TEXT = "#aaa"

COLOUR_BUTTON_NORMAL = "#5fba7d"
COLOUR_BUTTON_ACTIVE = "#58c77c"
COLOUR_BUTTON_PRESSED = "#44e378"


class ChatApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chat App")
        self.resizable(False, False)
        self.handle_messages = HandleMessages()
        self.message_display = DisplayMessages(self)
        self.message_sender = SendMessage(self)

        self.message_display.pack(fill="x")
        self.message_sender.pack()

    def handle_message_display(self):
        self.messages = self.handle_messages.get_messages()
        self.message_display.add_messages(self.messages)

    def handle_send_message(self):
        message = self.message_sender.message_box.get("1.0", "end")
        self.handle_messages.send_message(message)
        message = {
            "message": message,
            "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        }
        self.message_display.add_messages([message])
        self.message_sender.message_box.delete("1.0", "end")


if __name__ == "__main__":
    chat_app = ChatApp()

    font.nametofont("TkDefaultFont").configure(size=14)

    style = ttk.Style(chat_app)
    style.theme_use("clam")

    style.configure("Test.TFrame", background="red")
    style.configure("Test.TCanvas", background="red")
    style.configure("Messages.TFrame", background=COLOUR_LIGHT_BACKGROUND_3)

    style.configure("Controls.TFrame", background=COLOUR_LIGHT_BACKGROUND_2)

    style.configure(
        "SendButton.TButton", borderwidth=0, background=COLOUR_BUTTON_NORMAL
    )
    style.map(
        "SendButton.TButton",
        background=[
            ("pressed", COLOUR_BUTTON_PRESSED),
            ("active", COLOUR_BUTTON_ACTIVE),
        ],
    )

    style.configure(
        "FetchButton.TButton",
        background=COLOUR_LIGHT_BACKGROUND_1,
        borderwidth=0,
    )

    style.configure(
        "Time.TLabel",
        padding=5,
        background=COLOUR_LIGHT_BACKGROUND_1,
        foreground=COLOUR_LIGHT_TEXT,
        font=8,
    )

    style.configure("Avatar.TLabel", background=COLOUR_LIGHT_BACKGROUND_3)
    style.configure("Message.TLabel", background=COLOUR_LIGHT_BACKGROUND_2)
    chat_app.mainloop()
