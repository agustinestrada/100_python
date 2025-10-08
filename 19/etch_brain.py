from turtle import Turtle, Screen

cursor = Turtle()
screen = Screen()

class Control:

    def __init__(self,punto,pantalla):
        self.punto = punto
        self.pantalla = pantalla

    def move_forward(self):
        self.punto.forward(10)

    def move_backwards(self):
        self.punto.backwards(10)

    def turn_left(self):
        self.punto.left(10)

    def turn_right(self):
        self.punto.right(10)

    def turn_around(self):
        self.punto.left(180)

    def terminar(self):
        self.pantalla.bye()

    def clear(self):
        self.punto.clear()
        self.punto.penup()
        self.punto.home()
        self.punto.pendown()

control_cursor = Control(cursor,screen)