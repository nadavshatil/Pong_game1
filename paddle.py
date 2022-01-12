from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(position)


    def move_up(self):
        y = self.ycor()
        y += 25
        self.sety(y)

    def move_down(self):
        y = self.ycor()
        y -= 25
        self.sety(y)




