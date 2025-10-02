# Diccionarios

# Estan formados por "KEY" y "VALUE"
# KEY es el nombre de la propiedad
# VALUE es la data que esta asociada a esa KEY
# Ambos KEY y VALUE pueden ser cualquier tipo de dato (strings, ints,variables, booleans)


# {KEY:VALUE}

#        O BIEN 👇

# {
#     KEY:VALUE1,
#     KEY2:VALUE2,
#     KEY3:VALUE3,
# }

colours = {
    'apple': 'red',
    'pears': 'green',
    'banana': 'yellow'
}

colours2 = {
    'apple': 'red',
    'pears': 'green',
    'banana': 'yellow'
}

# print(colours[True])

# Para agregar un KEY/VALUE a un diccionario es de la siguiente manera
colours['key'] = 'value'
# Se le pasa entre corchetes la KEY que queremos agregar y mediante un igual le asignamos un valor

colours['kiwi'] = 'brown'

# Crear un diccionario vacio para llenarlo despues
empty_dictionary = {}

# Borrar todo lo que tenga un diccionario
# colours2 = {}

# Editar un diccionario es igual que crear un key nuevo pero con un key ya existente

colours2['pears'] = 'marble'

print(colours)
print(colours2)



