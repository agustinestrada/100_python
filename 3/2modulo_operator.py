# Modulo Operator %
# Nos da el Resto de una division sin la parte decimal, util para ver si un numero es par o impar

# 10 / 2 = 5, Resto o Modulo = 0
# 11 / 2 = 5, Resto o Modulo = 1

number_to_check = int(input('Escriba el numbero que quiere comprobar si es Par o Impar\n'))

if number_to_check % 2 == 0:
    print(f'{number_to_check} es un numero par')
else:
    print(f'{number_to_check} es un numero impar') 