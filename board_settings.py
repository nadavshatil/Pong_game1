from turtle import Turtle
class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.player_1_score = 0
        self.player_2_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-10, 250)
        self.update_score()
        self.boarder_line()

    def update_score(self):
        self.write(f"{self.player_1_score}            {self.player_2_score}", False, "center", ('David', 40, 'normal'))

    def add_score_player_a(self):
        self.player_1_score += 1
        self.clear()
        self.update_score()

    def add_score_player_b(self):
        self.player_2_score += 1
        self.clear()
        self.update_score()
    def player_1_win(self):
        self.home()
        self.color("green")
        self.write("Player 1 Wins!", False, "center", ('David', 50, 'normal'))
    def player_2_win(self):
        self.home()
        self.color("green")
        self.write("Player 2 Wins!", False, "center", ('David', 50, 'normal'))
    def boarder_line(self):
        boarder = Turtle()
        boarder.hideturtle()
        boarder.speed("fastest")
        boarder.color("white")
        boarder.goto(0, 300)
        boarder.width(30)
        boarder.goto(0, -300)



