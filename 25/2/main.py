# Iniciar con los imports necesarios
from turtle import Screen, Turtle
import pandas

# Inicializar los imports
screen = Screen()
screen.setup(width=740,height=500)

# Poner el mapa de USA de fondo
screen.bgpic('blank_states_img.gif')

# Leer el archivo CSV
data = pandas.read_csv('./50_states.csv')

# Aislar la columna de los estados para poder buscar despues
lista_de_estados = data['state'].to_list()

# Pedir al usuario que escriba el nombre de un estado


while len(lista_de_estados) > 0:
    estado = screen.textinput(title='States Game',prompt='Indique el nombre de un Estado').capitalize()
    # Validar si ese estado existe en la lista
    if lista_de_estados.count(estado.capitalize()):
        # Crear las cordenadas para el GOTO de Turtle
        estado_coordenadas = []
        estado_aislado = data[data['state'] == estado]
        estado_coordenadas.append(int(estado_aislado['x'].values[0]))
        estado_coordenadas.append(int(estado_aislado['y'].values[0]))

        # Crear tortuga y desplazarla a las coordenadas del CSV
        imprimir_estado = Turtle()
        imprimir_estado.hideturtle()
        imprimir_estado.penup()
        imprimir_estado.goto(estado_coordenadas[0],estado_coordenadas[1])
        imprimir_estado.write(estado,align='center',font=('Courier',8,'bold'))


        lista_de_estados.remove(estado)




screen.exitonclick()