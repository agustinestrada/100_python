def add(n1,n2):
    return n1 + n2

def substract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1 / n2

# Eleccion y validacion de operacion
eleccion = input('Por favor indique que operacion quiere hacer S,R,M,D\n')

while not(eleccion == 'S' or eleccion == 'R' or eleccion == 'M' or eleccion == 'D'):
    print('Por favor eliga una operacion valida')
    eleccion = input('Por favor indique que operacion quiere hacer S,R,M,D\n')

primer_numero = int(input('Ingrese el primer numero\n'))
segundo_numero = int(input('Ingrese el segundo numero\n'))

def operacion(elec):
    if elec == 'S':
        print(f'la suma es {add(primer_numero,segundo_numero)}')
    elif elec == 'R':
        print(f'la resta es {substract(primer_numero,segundo_numero)}')
    elif elec == 'M':
        print(f'la multiplicacion es {multiply(primer_numero,segundo_numero)}')
    elif elec == 'D':
        print(f'la division es {divide(primer_numero,segundo_numero)}')


operacion(eleccion)