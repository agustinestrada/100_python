print('Bienvenido a Python Pizza Delivery')
tamano = input('De que tamaño va a querer la pizza? G, M, C\n')

cuenta = 0

pc = 15
pm = 20
pg = 25

if tamano == "C" or tamano == "G" or tamano == "M":
    pepperoni = input('Quiere pepperoni por $2 mas en la Chica y $3 mas en la Mediana y Grande?\n')
    queso_extra = input('Quiere queso extra por $1 mas? Y o N\n')
    if tamano == "C":
        cuenta = pc
        if pepperoni == "Y":
            cuenta += 2
    elif tamano == "M":
        cuenta = pm
        if pepperoni == "Y":
            cuenta += 3
    elif tamano == "G":
        cuenta = pg
        if pepperoni == "Y":
            cuenta += 3     
    if queso_extra == 'Y':
        cuenta += 1
    print(f'Su cuenta es de {cuenta}')

else:
    print('Su opcion no fue registrada con exito')