print('Welcome to the Rollercoaster!')
altura = int(input('Por favor introduzca su altura en centimetros\n'))
edad = int(input('Por favor introduzca su edad\n'))

if altura < 120: # Es importante ponerle el ":" para terminar
    print('Sorry, no podes subir')
else: # Es importante ponerle el ":" para terminar
    if edad <= 12:
        print('Pasa tranqui, el boleto es de $5')
    elif edad <= 18:
        print('Pasa tranqui, el boleto es de $7')
    else:
        print('Pasa tranqui, el boleto es de $12')
