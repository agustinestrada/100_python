from turtle import Turtle, Screen

tim = Turtle()
tom = Turtle()
tim.color('red')
tom.color('green')
screen = Screen()
#tim.shape('turtle')

class Movimiento:

    def __init__(self,tortuga):
        self.tortuga = tortuga

    def move_foward(self):
        self.tortuga.forward(10)

    def turn_right(self):
        self.tortuga.right(90)

    def turn_left(self):
        self.tortuga.left(90)

    def turn_around(self):
        self.tortuga.left(180)

    def walk_backwards(self):
        self.tortuga.forward(-10)

    def clear_canva(self):
        self.tortuga.clear()

    def levantar(self):
        self.tortuga.penup()

    def escribir(self):
        self.tortuga.pendown()

screen.listen()


screen.onkey(key='w',fun=move_foward)
screen.onkey(key='s',fun=walk_backwards)
screen.onkey(key='d',fun=turn_right)
screen.onkey(key='a',fun=turn_left)
screen.onkey(key='space',fun=turn_around)
screen.onkey(key='c',fun=clear_canva)
screen.onkey(key='Escape',fun=screen.bye)
screen.onkey(key='Up',fun=levantar)
screen.onkey(key='Down',fun=escribir)



