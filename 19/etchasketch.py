from turtle import Turtle, Screen
from etch_brain import control_cursor

screen = Screen()

screen.listen()

screen.onkey(control_cursor.move_forward,'w')
screen.onkey(control_cursor.move_backwards,'s')
screen.onkey(control_cursor.turn_left,'a')
screen.onkey(control_cursor.turn_right,'d')
screen.onkey(control_cursor.turn_around,'t')
screen.onkey(control_cursor.terminar,'Escape')
screen.onkey(control_cursor.clear,'h')

screen.exitonclick()