from turtle import Turtle

class Escribir(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('red')
        self.game_over = 'GAME OVER'
        self.right_won = 'Right player Won!'
        self.left_won = 'Left player Won!'