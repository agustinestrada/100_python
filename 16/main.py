# from turtle import Turtle, Screen

# timmy = Turtle()
# my_screen = Screen()
# timmy.shape("turtle")
# timmy.color("aquamarine")
# timmy.forward(100)

# print(timmy)
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
frutas = ["manzana", "banana", "cereza", "naranja", "uva"]

tabla = PrettyTable()
tabla.add_column('Frutas', frutas)
print(tabla)