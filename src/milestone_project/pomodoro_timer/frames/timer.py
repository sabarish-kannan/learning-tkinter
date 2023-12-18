import tkinter as tk
from tkinter import ttk


class Timer(ttk.Frame):
    def __init__(self, container, settings):
        super().__init__(container)
        self["style"] = "Background.TFrame"
        self.container = container
        # self.columnconfigure(0, weight=1)

        pomodoro_time = int(container.pomodoro_time.get())
        self.current_time = tk.StringVar(value=f"{pomodoro_time:02d}:00")
        self.is_timer_running = False

        top_frame = ttk.Frame(self, style="Background.TFrame")
        top_frame.grid(row=0, column=0, sticky="EW", pady=(10, 0))
        top_frame.columnconfigure(0, weight=1)

        timer_label = ttk.Label(
            top_frame,
            textvariable=container.current_event,
            style="LightText.TLabel",
        )
        timer_label.grid(
            row=0, column=0, sticky="W", padx=(10, 10), pady=(0, 10)
        )
        settings_button = ttk.Button(
            top_frame,
            text="Settings",
            cursor="hand2",
            command=settings,
            style="PomodoroButton.TButton",
        )
        settings_button.grid(
            row=0, column=1, sticky="E", padx=(0, 10), pady=(0, 10)
        )

        middle_frame = ttk.Frame(self)
        middle_frame.grid(row=1, column=0, sticky="EW")
        middle_frame.columnconfigure(0, weight=1)

        timer = ttk.Label(
            middle_frame,
            textvariable=self.current_time,
            anchor="center",
            style="Timer.TLabel",
            padding=25,
        )
        timer.grid(row=0, column=0, sticky="EW")

        bottom_frame = ttk.Frame(self, style="Background.TFrame")
        bottom_frame.grid(row=2, column=0, sticky="EW", pady=(15, 15))
        # bottom_frame.columnconfigure(0, weight=1)
        # bottom_frame.columnconfigure(1, weight=1)
        # bottom_frame.columnconfigure(2, weight=1)

        self.start_button = ttk.Button(
            bottom_frame,
            text="Start",
            command=self.start_timer,
            cursor="hand2",
            style="PomodoroButton.TButton",
        )
        self.start_button.grid(row=0, column=0, padx=10)
        self.stop_button = ttk.Button(
            bottom_frame,
            text="Stop",
            command=self.stop_timer,
            cursor="hand2",
            state="disabled",
            style="PomodoroButton.TButton",
        )
        self.stop_button.grid(row=0, column=1, padx=10)
        reset_button = ttk.Button(
            bottom_frame,
            text="Reset",
            command=self.reset_timer,
            cursor="hand2",
            style="PomodoroButton.TButton",
        )
        reset_button.grid(row=0, column=2, padx=10)

        self.run_timer()

    def run_timer(self):
        current_time = self.current_time.get()
        if self.is_timer_running and current_time != "00:00":
            mins, secs = map(int, current_time.split(":"))
            if secs != 0:
                secs -= 1
                self.current_time.set(f"{mins:02d}:{secs:02d}")
            else:
                secs = 59
                mins -= 1
                self.current_time.set(f"{mins:02d}:{secs:02d}")
            self.after(1000, self.run_timer)
        elif self.is_timer_running and current_time == "00:00":
            old_event = self.container.timer_schedule.pop(0)
            self.container.timer_schedule.append(old_event)
            next_event = self.container.timer_schedule[0]
            self.container.current_event.set(next_event)

            if next_event == "Pomodoro":
                pomodoro_time = int(self.container.pomodoro_time.get())
                self.current_time.set(f"{pomodoro_time:02d}:00")
            elif next_event == "Short break":
                short_break_time = int(self.container.short_break.get())
                self.current_time.set(f"{short_break_time:02d}:00")
            elif next_event == "Long break":
                long_break_time = int(self.container.long_break.get())
                self.current_time.set(f"{long_break_time:02d}:00")
            self.after(1000, self.run_timer)

    def start_timer(self):
        self.is_timer_running = True
        self.start_button["state"] = "disabled"
        self.stop_button["state"] = "normal"
        self.run_timer()

    def stop_timer(self):
        self.is_timer_running = False
        self.start_button["state"] = "normal"
        self.stop_button["state"] = "disabled"

    def reset_timer(self):
        pomodoro_time = int(self.container.pomodoro_time.get())
        self.current_time.set(f"{pomodoro_time:02d}:00")
        self.container.timer_schedule = self.container.timer_order.copy()
        self.container.current_event.set(self.container.timer_schedule[0])
        self.stop_timer()
