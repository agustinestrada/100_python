import string
import sys
import random

# # 1. Todas las letras en mayúscula y minúscula
# letras = [
#     'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
#     'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
# ]

# # 2. Números del 0 al 9 (como strings)
# numeros = ['0','1','2','3','4','5','6','7','8','9']

# # 3. Símbolos (los de string.punctuation, en orden ASCII)
# simbolos = [
#     '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', 
#     ':', ';', '<', '=', '>', '?', '@', 
#     '[', '\\', ']', '^', '_', '`', 
#     '{', '|', '}', '~'
# ]


# La funcion list() crea una lista/array con un objeto iterable: strings, tuplas, diccionarios, sets,rangos, etc...

letras2 = list(string.ascii_letters)
numeros2 = list(string.digits)
simbolos2 = list(string.punctuation)

contrasena = ''

# print(letras)
# print(numeros)
# print(simbolos)

cantidad_de_caracteres = int(input('Escriba la cantidad de caracteres que quiere para su contraseña\n'))
cantidad_de_simbolos = int(input('Escriba la cantidad de simbolos que quiere en su contraseña\n'))
cantidad_de_numeros = int(input('Escriba la cantidad de numeros que quiere en su contraseña\n'))
cantidad_de_letras = cantidad_de_caracteres - (cantidad_de_numeros + cantidad_de_simbolos)


if cantidad_de_letras <= 0:
    print('La contraseña no se pudo generar correctamente')
    sys.exit()

# print(cantidad_de_caracteres)
# print(cantidad_de_simbolos)
# print(cantidad_de_numeros)
# print(cantidad_de_letras)

# for number in range(1,cantidad_de_letras+1):
#     contrasena += letras2[random.randint(0,len(letras2))]

# for number in range(1,cantidad_de_simbolos+1):
#     contrasena += simbolos2[random.randint(0,len(simbolos2))]

# for number in range(1,cantidad_de_numeros+1):
#     contrasena += numeros2[random.randint(0,len(numeros2))]

for number in range(1, cantidad_de_letras+1):
    contrasena += random.choice(letras2)

for number in range(1, cantidad_de_numeros+1):
    contrasena += random.choice(numeros2)

for number in range(1, cantidad_de_simbolos+1):
    contrasena += random.choice(simbolos2)

print(contrasena)