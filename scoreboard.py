from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # High score ku store karna
        with open("data.txt") as file:
            con = file.read()
            self.high_score = int(con)
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_write()

    def update_write(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_write()

    def increase_score(self):
        self.score += 1
        self.update_write()
