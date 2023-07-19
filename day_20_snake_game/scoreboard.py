from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.score = 0
        self.penup()
        self.goto(-20, 260)
        self.color("white")
        self.hideturtle()
        with open("high_score.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.write(f"\tScore: {self.score}              High Score: {self.high_score}", False, align="center", font=("Arial", 16, "normal"))

    def increment_score(self):
        self.score = self.score + 1
        self.clear()
        self.write(f"\tScore: {self.score}              High Score: {self.high_score}", False, align="center", font=("Arial", 16, "normal"))

    def update_board(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as file:
                file.write(self.high_score.__str__())
        self.score = 0
        self.write(f"\tScore: {self.score}              High Score: {self.high_score}", False, align="center", font=("Arial", 16, "normal"))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game over.", False, align="center", font=("Arial", 16, "normal"))
