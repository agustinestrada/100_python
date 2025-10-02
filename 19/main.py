from turtle import Turtle, Screen   

screen = Screen()
screen.listen()

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

screen.listen()

# Creamos controladores para cada tortuga
control_tim = Movimiento(tim)
control_tom = Movimiento(tom)

# Asignamos teclas a la tortuga "tim"
screen.onkey(control_tim.move_foward, "w")
screen.onkey(control_tim.walk_backwards, "s")
screen.onkey(control_tim.turn_right, "d")
screen.onkey(control_tim.turn_left, "a")

# Asignamos teclas a la tortuga "tom"
screen.onkey(control_tom.move_foward, "Up")
screen.onkey(control_tom.walk_backwards, "Down")
screen.onkey(control_tom.turn_right, "Right")
screen.onkey(control_tom.turn_left, "Left")

# Otros comandos
screen.onkey(clear_canva, "c")
screen.onkey(screen.bye, "Escape")  # cerrar ventana con Escape

screen.mainloop()