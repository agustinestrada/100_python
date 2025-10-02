import string
import random

letras = list(string.ascii_letters)
numeros = list(string.digits)
simbolos = list(string.punctuation)

cantidad_de_caracteres = int(input('Escriba la cantidad de caracteres que quiere para su contraseña\n'))
cantidad_de_simbolos = int(input('Escriba la cantidad de simbolos que quiere en su contraseña\n'))
cantidad_de_numeros = int(input('Escriba la cantidad de numeros que quiere en su contraseña\n'))
cantidad_de_letras = cantidad_de_caracteres - (cantidad_de_numeros + cantidad_de_simbolos)

contrasena = []

for number in range(0, cantidad_de_letras):
    contrasena.append(random.choice(letras))

for number in range(0, cantidad_de_numeros):
    contrasena.append(random.choice(numeros))

for number in range(0, cantidad_de_simbolos):
    contrasena.append(random.choice(simbolos))

random.shuffle(contrasena)

# contrasena2 = contrasena

contrasena = ''.join(contrasena)
# contrasena2 =  str(contrasena2)

print(contrasena)
# print(contrasena2)
