from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from messages import Escribir
import time
TOP_BORDER = 250
BOTTOM_BORDER = -250
RIGHT_BORDER = 380
LEFT_BORDER = -380
FONT = ('Courier',18,'bold')
ALIGNMENT = 'center'


screen = Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.tracer(0)

r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()
message = Escribir()

screen.listen()
screen.onkey(r_paddle.go_up,'Up')
screen.onkey(r_paddle.go_down,'Down')
screen.onkey(l_paddle.go_up,'w')
screen.onkey(l_paddle.go_down,'s')
game_is_on = True

while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() > TOP_BORDER or ball.ycor() < BOTTOM_BORDER:
        ball.bounce()

    #Detect collision with r_paddle
    right_collition = ball.distance(r_paddle) < 50 and ball.xcor() > 320
    left_collition = ball.distance(l_paddle) < 50 and ball.xcor() < -320

    if right_collition or left_collition:
        ball.paddle_bounce()
    elif ball.xcor() < LEFT_BORDER or ball.xcor() > RIGHT_BORDER:
        game_is_on = False
        if ball.xcor() < 0:
            message.write(arg=f'{message.right_won}',align=ALIGNMENT,font=FONT)
        elif ball.xcor() > 0:
            message.write(arg=f'{message.left_won}',align=ALIGNMENT,font=FONT)


screen.exitonclick()