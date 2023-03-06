from random import choice, randint
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self) -> None:
        self.cars: list[Car] = []
        self.speed = MOVE_INCREMENT

    def generate_car(self):
        self.cars.append(Car())

    def move_cars(self) -> None:
        for car in self.cars:
            car.move_y(self.speed)

    def increase_speed(self) -> None:
        self.speed += 1

    def detect_collision(self, xcor: float, ycor: float) -> bool:
        for car in self.cars:
            if abs(car.xcor() - xcor) < 30 and abs(car.ycor() - ycor) < 20:
                return True
        return False


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(choice(COLORS))
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.goto(300, randint(-250, 250))

    def move_y(self, distance: int) -> None:
        self.goto(self.xcor() - distance, self.ycor())
