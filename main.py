from turtle import Screen
from player import Player
import LevelController
import time

STARTING_LEVEL = 0

screen = Screen()
screen.setup(width=600, height=800)
screen.bgpic("simplelanes.gif")
screen.title("Toadster")
screen.tracer(0)

toadster = Player()

level_controller = LevelController.Level()

screen.listen()
screen.onkey(toadster.move_up, "Up")
screen.onkey(toadster.move_down, "Down")
screen.onkey(toadster.move_left, "Left")
screen.onkey(toadster.move_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    if toadster.ycor() >= 380:
        if level_controller.level_number == 6:
            level_controller.win_screen()
            game_is_on = False
        else:
            toadster.reset_player()
            level_controller.update_level_number()
    for opp in level_controller.all_the_opps:
        opp.cross_street()
        if toadster.distance(opp) < 15:
            level_controller.lose_screen()
            game_is_on = False







screen.exitonclick()
