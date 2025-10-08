from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500,height=400)

# bet = input('Pick your favourite turtle to win').lower()
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ').lower() # Devuelve un string

tim = Turtle(shape='turtle')
tim.goto(x=-230, y=-100)

screen.exitonclick()