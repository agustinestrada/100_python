from turtle import Turtle, Screen

tim = Turtle()
tom = Turtle()
tim.color('red')
tom.color('green')
screen = Screen()
#tim.shape('turtle')


def move_foward():
    tim.forward(10)

def turn_right():
    tim.right(90)

def turn_left():
    tim.left(90)

def turn_around():
    tim.left(180)

def walk_backwards():
    tim.forward(-10)

def clear_canva():
    tim.clear()

def levantar():
    tim.penup()

def escribir():
    tim.pendown()

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



screen.exitonclick()