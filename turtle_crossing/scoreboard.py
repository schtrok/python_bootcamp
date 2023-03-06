from turtle import Turtle

SCORE_FONT = ("Courier", 24, "normal")
GAME_OVER_FONT = ("Courier", 30, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)
        self.update()

    def update(self, player_level: int = 1) -> None:
        self.clear()
        self.write(f"Level: {player_level}", align="left", font=SCORE_FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over!", align="center", font=GAME_OVER_FONT)
