from turtle import Turtle


class Line(Turtle):
    def __init__(self, ycor: int):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-300, ycor)

        for step in range(-300, 300, 20):
            self.pendown() if not self.pen().get("pendown") else self.penup()
            self.goto(step, self.ycor())
