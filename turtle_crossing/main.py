import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard
from line import Line

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
start_line = Line(-250)
finish_line = Line(250)

screen.listen()
screen.onkeypress(player.move, "Up")


game_is_on: bool = True
iteration: int = 0

while game_is_on:
    # check if we generate a new car
    if iteration % 6 == 0:
        car_manager.generate_car()

    # move all existing cars
    car_manager.move_cars()

    # check win condition
    if player.ycor() > 250:
        time.sleep(0.7)
        player.level_up()
        scoreboard.update(player.level)

    if car_manager.detect_collision(player.xcor(), player.ycor()):
        scoreboard.game_over()
        player.reset()
        break

    time.sleep(0.1)
    screen.update()
    iteration += 1

screen.exitonclick()
