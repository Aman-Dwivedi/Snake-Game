from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Times New Roman", 14, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.setposition(0, 275)
        self.score = 0
        with open("data.txt", 'r') as data:
            high_score = int(data.read())
            self.high_score = high_score
        self.write_score()
        self.hideturtle()

    def update_score(self):
        self.score += 1
        self.write_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", 'w') as data:
                data.write(str(self.high_score))
        self.score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",
                   align=ALIGNMENT, font=FONT)
