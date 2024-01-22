from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 48, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0


