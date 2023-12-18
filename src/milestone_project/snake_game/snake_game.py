import sys
from os import path
from random import randint
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


MOVE_INCREMENT = 20
moves_per_second = 15
GAME_SPEED = 1000 // moves_per_second


class Snake(tk.Canvas):
    def __init__(self):
        super().__init__(
            width=600, height=620, background="black", highlightthickness=0
        )

        self.snake_positions = [(100, 100), (80, 100), (60, 100)]
        self.food_position = (180, 100)
        self.direction = "Right"
        self.score = 0
        self.moves_per_second = moves_per_second
        self.bind_all("<Key>", self.control_snake)
        self.create_image_objects()
        self.create_objects()
        self.move_snake()

        self.pack()

    def create_image_objects(self):
        try:
            bundle_dir = getattr(
                sys, "_MEIPASS", path.abspath(path.dirname(__file__))
            )
            snake_image_path = path.join(bundle_dir, "images", "snake.png")
            snake_body = Image.open(snake_image_path)
            self.snake_body = ImageTk.PhotoImage(snake_body)
            food_image_path = path.join(bundle_dir, "images", "food.png")
            food = Image.open(food_image_path)
            self.food = ImageTk.PhotoImage(food)
        except IOError as error:
            print(error)
            app.destroy()

    def create_objects(self):
        self.create_text(
            75,
            12,
            text=f"Score: {self.score}\t Speed: {self.moves_per_second}",
            tag="score",
            fill="#fff",
            font=10,
        )
        for snake_position in self.snake_positions:
            self.create_image(
                *snake_position, image=self.snake_body, tag="snake"
            )
        self.create_image(*self.food_position, image=self.food, tag="food")
        self.create_rectangle(7, 27, 593, 613, outline="#525d69")

    def move_snake(self):
        head_x_position, head_y_position = self.snake_positions[0]
        new_position = ()
        if self.direction == "Right":
            new_position = (head_x_position + MOVE_INCREMENT, head_y_position)
        elif self.direction == "Left":
            new_position = (head_x_position - MOVE_INCREMENT, head_y_position)
        elif self.direction == "Down":
            new_position = (head_x_position, head_y_position + MOVE_INCREMENT)
        elif self.direction == "Up":
            new_position = (head_x_position, head_y_position - MOVE_INCREMENT)
        self.snake_positions = [new_position] + self.snake_positions[:-1]

        if self.check_collision():
            self.end_game()
            return

        self.food_collision()

        for segment, position in zip(
            self.find_withtag("snake"), self.snake_positions
        ):
            self.coords(segment, position)
        self.after(GAME_SPEED, self.move_snake)

    def check_collision(self):
        snake_head_position = self.snake_positions[0]
        return (
            snake_head_position in self.snake_positions[1:]
            or snake_head_position[0] in (0, 600)
            or snake_head_position[1] in (20, 620)
        )

    def control_snake(self, event):
        direction = event.keysym
        all_directions = ("Right", "Left", "Up", "Down")
        opposite_directions = [{"Left", "Right"}, {"Up", "Down"}]

        if (
            direction in all_directions
            and {direction, self.direction} not in opposite_directions
        ):
            self.direction = direction

    def food_collision(self):
        snake_head_position = self.snake_positions[0]
        if snake_head_position == self.food_position:
            self.score += 1
            if self.score % 5 == 0:
                self.moves_per_second += 5
            self.snake_positions.append(self.snake_positions[-1])
            self.create_image(
                *self.snake_positions[-1], image=self.snake_body, tag="snake"
            )
            self.set_new_food_position()
            food = self.find_withtag("food")
            self.coords(food, self.food_position)
            score = self.find_withtag("score")
            self.itemconfigure(
                score,
                text=f"Score: {self.score}\t Speed: {self.moves_per_second}",
            )

    def set_new_food_position(self):
        while True:
            x_position = randint(1, 29) * MOVE_INCREMENT
            y_position = randint(3, 30) * MOVE_INCREMENT
            new_position = (x_position, y_position)
            if new_position not in self.snake_positions:
                self.food_position = new_position
                break

    def end_game(self):
        self.delete(tk.ALL)
        self.create_text(
            self.winfo_width() / 2,
            self.winfo_height() / 2,
            text=f"Game Over. Your score is {self.score}",
            fill="#fff",
            font=15,
        )
        button_frame = ttk.Frame(self, style="Buttons.TFrame")
        retry_button = ttk.Button(
            button_frame,
            text="Retry",
            command=self.retry,
            style="Buttons.TButton",
            cursor="hand2",
        )
        quit_button = ttk.Button(
            button_frame,
            text="Quit",
            command=app.destroy,
            style="Buttons.TButton",
            cursor="hand2",
        )
        retry_button.pack(side="left", padx=20)
        quit_button.pack(side="left", padx=20)
        button_window = self.create_window(
            self.winfo_width() / 2,
            (self.winfo_height() / 2) + 50,
            anchor="center",
            window=button_frame,
        )

    def retry(self):
        self.destroy()
        self.__init__()


app = tk.Tk()
app.title("Sname Game")
app.resizable(False, False)

style = ttk.Style(app)
style.theme_use("clam")
style.configure("Buttons.TButton", background="#fff")
style.configure("Buttons.TFrame", background="#000")

Snake()

app.mainloop()
