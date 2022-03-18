from turtle import Turtle


class score(Turtle):
    def __init__(self):

        super().__init__()
        with open("snake_high_score.txt") as file:
            contents = file.read()
        self.highScore = contents
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(0, 280)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} || HighScore : {self.highScore}",
                   False, "center", ("Arial", 8, "normal"))

    def score_increment(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        if self.score > int(self.highScore):
            with open("snake_high_score.txt", mode="w") as file:
                file.write(str(self.score))
            with open("snake_high_score.txt") as file:
                contents = file.read()
            self.highScore = contents
        self.score = 0
        self.update_score()
