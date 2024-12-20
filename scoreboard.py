from turtle import Turtle
FONT = ('Terminal', 11 , 'normal')
ALIGN = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed = 1
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.highscore}", align=ALIGN, font=FONT)

    def red_score(self):
        """Adds double points for red food."""
        self.score += 10
        self.update_scoreboard()

    def blue_score(self):
        """Adds single point for blue food."""
        self.score += 5
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align=ALIGN, font=FONT)
        if self.score > self.highscore:
            self.goto(0, -20)
            self.write(arg=f"NEW HIGH SCORE : {self.score}", align=ALIGN, font=FONT)
        self.reset()
