from opps import Opps
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
OBSTACLES_PER_LEVEL = [0, 8, 10, 12, 14, 16, 25]


def spawn_number_of_opps_for_level(level):
    all_the_opps = []
    for opp in range(OBSTACLES_PER_LEVEL[level]):
        new_opp = Opps()
        all_the_opps.append(new_opp)
    return all_the_opps


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.color("black")
        self.hideturtle()
        self.level_number = 0
        self.all_the_opps = []
        self.all_the_opps = self.update_level_number()

    def update_level_number(self):
        for opp in self.all_the_opps:
            opp.hideturtle()
        self.clear()
        self.level_number += 1
        self.goto(200, 360)
        self.write(f"Level {self.level_number}", font=FONT, align=ALIGNMENT)
        all_the_opps = spawn_number_of_opps_for_level(self.level_number)
        self.all_the_opps = all_the_opps
        return all_the_opps

    def win_screen(self):
        self.clear()
        self.goto(0, 360)
        self.write(f"You won !", font=FONT, align=ALIGNMENT)

    def lose_screen(self):
        self.clear()
        self.goto(0, 360)
        self.write(f"You lose !", font=FONT, align=ALIGNMENT)
