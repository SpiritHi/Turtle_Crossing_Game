from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.left(90)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.backward(MOVE_DISTANCE)

    def turn_left(self):
        self.left(90)
        self.forward(10)
        self.right(90)

    def turn_right(self):
        self.right(90)
        self.forward(10)
        self.left(90)

    def respawn(self):
        self.goto(STARTING_POSITION)
