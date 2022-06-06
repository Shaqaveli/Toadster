from turtle import Turtle

JUMP_AMOUNT = 15
STARTING_POSITION = (0, -370)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("circle")
        self.color("green")
        self.seth(90)
        self.reset_player()
        self.shapesize(stretch_wid=1.2, stretch_len=1.2)

    def move_up(self):
        new_ycor = self.ycor() + JUMP_AMOUNT
        self.setpos(self.xcor(), new_ycor)

    def move_down(self):
        new_ycor = self.ycor() - JUMP_AMOUNT
        self.setpos(self.xcor(), new_ycor)

    def move_left(self):
        new_xcor = self.xcor() - JUMP_AMOUNT
        self.setpos(new_xcor, self.ycor())

    def move_right(self):
        new_xcor = self.xcor() + JUMP_AMOUNT
        self.setpos(new_xcor, self.ycor())

    def reset_player(self):
        self.setpos(STARTING_POSITION)
