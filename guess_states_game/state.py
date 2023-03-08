from turtle import Turtle

STATE_FONT = ("Courier", 10, "bold")


class State(Turtle):
    def __init__(self, name: str, x: float, y: float):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x, y)

        self.write(name, align="center", font=STATE_FONT)
