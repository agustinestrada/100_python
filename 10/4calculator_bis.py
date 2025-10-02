from operaciones import *

# Eleccion y validacion de operacion
eleccion = input('Por favor indique que operacion quiere hacer +,-,*,/\n')

primer_numero = int(input('Ingrese el primer numero\n'))
segundo_numero = int(input('Ingrese el segundo numero\n'))

operacion = {
    '+': add,
    '-': substract,
    '*': multiply,
    '/': divide 
}

# def calculator(elec):
#     if elec == 'S':
#         print(f'la suma es {add(primer_numero,segundo_numero)}')
#     elif elec == 'R':
#         print(f'la resta es {substract(primer_numero,segundo_numero)}')
#     elif elec == 'M':
#         print(f'la multiplicacion es {multiply(primer_numero,segundo_numero)}')
#     elif elec == 'D':
#         print(f'la division es {divide(primer_numero,segundo_numero)}')
# calculator(eleccion)

# Forma facil y corta de hacerlo
operacion[eleccion](primer_numero,segundo_numero)

# Forma larga de hacerlo
# for oper in operacion:
#     if eleccion == oper:
#         operacion[oper](primer_numero,segundo_numero)
