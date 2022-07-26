from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-260, 250)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.score} High Score: {self.high_score}", align="left", font=FONT)

    def score_point(self):
        self.score += 1
        self.update_score()

    def lost(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.clear()
        self.home()
        self.write(f"You lose. Score: {self.score}", align="center", font=FONT)

