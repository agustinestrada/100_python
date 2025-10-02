from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape('turtle')
timmy.color('red')
screen = Screen()

for i in range(1,5):
    timmy.forward(100)
    timmy.left(90)
    

# screen.exitonclick()