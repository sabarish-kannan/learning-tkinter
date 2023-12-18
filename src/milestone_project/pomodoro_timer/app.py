import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from frames.timer import Timer
from frames.settings import Settings
from windows import set_dpi_awareness

set_dpi_awareness()
COLOUR_PRIMARY = "#2e3f4f"
COLOUR_SECONDARY = "#293846"
COLOUR_LIGHT_BACKGROUND = "#fff"
COLOUR_LIGHT_TEXT = "#eee"
COLOUR_DARK_TEXT = "#8095a8"


class Pomodoro(tk.Tk):
    def __init__(self):
        super().__init__()

        # Style Sections
        font.nametofont("TkDefaultFont").configure(size=15)
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure(
            "Timer.TLabel",
            background=COLOUR_LIGHT_BACKGROUND,
            foreground=COLOUR_DARK_TEXT,
            font="Courier 38",
        )
        style.configure("Background.TFrame", background=COLOUR_PRIMARY)
        style.configure(
            "TimerText.TLabel",
            background=COLOUR_LIGHT_BACKGROUND,
            foreground=COLOUR_DARK_TEXT,
            font="Courier 38",
        )

        style.configure(
            "LightText.TLabel",
            background=COLOUR_PRIMARY,
            foreground=COLOUR_LIGHT_TEXT,
        )

        style.configure(
            "PomodoroButton.TButton",
            background=COLOUR_SECONDARY,
            foreground=COLOUR_LIGHT_TEXT,
        )

        style.map(
            "PomodoroButton.TButton",
            background=[
                ("active", COLOUR_PRIMARY),
                ("disabled", COLOUR_LIGHT_TEXT),
            ],
        )
        # style.configure("Test.TFrame", background="blue")

        self.pomodoro_time = tk.StringVar(value="25")
        self.short_break = tk.StringVar(value="5")
        self.long_break = tk.StringVar(value="15")
        self.timer_order = [
            "Pomodoro",
            "Short break",
            "Pomodoro",
            "Short break",
            "Pomodoro",
            "Long break",
        ]
        self.timer_schedule = self.timer_order.copy()
        self.current_event = tk.StringVar(value=self.timer_schedule[0])

        self.title("Pomodoro Timer")
        self.resizable(False, False)

        self.columnconfigure(0, weight=1)
        self.frames_dict = dict()
        setting_frame = Settings(self, lambda: self.switch_frame(Timer))
        setting_frame.grid(row=0, column=0, sticky="EW")
        timer_frame = Timer(self, lambda: self.switch_frame(Settings))
        timer_frame.grid(row=0, column=0, sticky="EW")
        self.frames_dict[Timer] = timer_frame
        self.frames_dict[Settings] = setting_frame

    def switch_frame(self, frame_name):
        self.frames_dict[frame_name].tkraise()


app = Pomodoro()

app.mainloop()
