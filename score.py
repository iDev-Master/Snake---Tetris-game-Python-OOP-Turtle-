from turtle import Turtle, write

SCORE = 0

# with open('highest_score.txt', mode="w") as data:
#     data.write('5')

notes = open('highest_score.txt')
highest_score_from_file = int(notes.read())
notes.close()


class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.highest_score = highest_score_from_file
        self.hideturtle()
        self.penup()
        self.goto(-100, 270)
        self.color('white')
        self.update_score()

    def update_score(self):    
        self.clear()
        self.write(f"Score = {self.score}   Highest Score: {self.highest_score}", font=("Arial", 12, "normal"))
    
    def reset(self):
        if self.score > int(self.highest_score):
            with open('highest_score.txt', mode="w") as result:
                result.write(f'{self.score}')

            self.highest_score = self.score
        self.score = 0
        self.update_score()

    
    def increase_score(self):
        self.score += 1
        self.update_score()



