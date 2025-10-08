from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ').lower() # Devuelve un string
all_turtles = []

if user_bet:
    is_race_on = True

colours = ['red','purple','blue','yellow','green','orange']
y_positions =[130, 80,30,-20,-70,-120]

for turtle_index in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colours[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

while is_race_on:

    end_of_game = 230

    for turtle in all_turtles:
        if turtle.xcor() > end_of_game:
            print(f"Winner is {turtle.pencolor()}")
            is_race_on = False
            if user_bet == turtle.pencolor():
                print('You Won!')
            else:
                print('You Lost!')


        rand_distance = randint(1,10)
        turtle.forward(rand_distance)


screen.exitonclick()