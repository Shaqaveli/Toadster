from turtle import Turtle
import random

STARTING_SIDES = [300, -300]
OPPS_COLORS = ["red", "orange", "blue", "purple", "yellow"]


class Opps(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.respawn()

    def respawn(self):
        self.color(random.choice(OPPS_COLORS))
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.setpos(random.choice(STARTING_SIDES), random.randint(-290, 290))
        self.turn_around()

    def cross_street(self):
        self.turn_around()
        move_speed = random.randint(10, 25)
        self.forward(move_speed)

    def turn_around(self):
        if self.xcor() >= 290:
            self.seth(180)
        elif self.xcor() <= -290:
            self.seth(0)

