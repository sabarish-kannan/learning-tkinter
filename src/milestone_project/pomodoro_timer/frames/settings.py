import tkinter as tk
from tkinter import ttk


class Settings(ttk.Frame):
    def __init__(self, container, back):
        super().__init__(container)
        self["style"] = "Background.TFrame"
        self.container = container
        self.columnconfigure(0, weight=1)

        self.frame = ttk.Frame(
            self, padding=(30, 40, 30, 40), style="Background.TFrame"
        )
        self.frame.grid(row=0, column=0)

        pomodoro_label = ttk.Label(
            self.frame,
            text="Pomodoro : ",
            style="LightText.TLabel",
        )
        short_break_label = ttk.Label(
            self.frame,
            text="Short Break time: ",
            style="LightText.TLabel",
        )
        long_break_label = ttk.Label(
            self.frame,
            text="Long Break time: ",
            style="LightText.TLabel",
        )
        pomodoro_input = ttk.Spinbox(
            self.frame,
            from_=0,
            to=120,
            justify="center",
            width=10,
            textvariable=container.pomodoro_time,
        )
        short_break_input = ttk.Spinbox(
            self.frame,
            from_=0,
            to=120,
            justify="center",
            width=10,
            textvariable=container.short_break,
        )
        long_break_input = ttk.Spinbox(
            self.frame,
            from_=0,
            to=120,
            justify="center",
            width=10,
            textvariable=container.long_break,
        )

        pomodoro_label.grid(row=0, column=0, sticky="W", padx=(40, 70))
        pomodoro_input.grid(row=0, column=1, sticky="E", padx=(20, 0))
        short_break_label.grid(row=1, column=0, sticky="W", padx=(40, 70))
        short_break_input.grid(row=1, column=1, sticky="E", padx=(20, 0))
        long_break_label.grid(row=2, column=0, sticky="W", padx=(40, 70))
        long_break_input.grid(row=2, column=1, sticky="E", padx=(20, 0))

        self.frame.columnconfigure(0, weight=1)
        back_button = ttk.Button(
            self.frame,
            text="← Back",
            cursor="hand2",
            command=back,
            style="PomodoroButton.TButton",
        )
        back_button.grid(
            row=3, column=0, sticky="EW", columnspan=2, pady=(25, 0), padx=60
        )
