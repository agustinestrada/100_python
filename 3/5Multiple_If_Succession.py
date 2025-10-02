print('Welcome to the Rollercoaster!')
altura = int(input('Por favor introduzca su altura en centimetros\n'))
bill = 0

if altura >= 120: # Es importante ponerle el ":" para terminar 
    
    edad = int(input('Por favor introduzca su edad\n'))
    
    print('Los valores son Menores de 13 $5, Menores de 19 $7, y Mayores $12')
    
    if edad <= 12:
        bill = 5
        #print(f'Pasa tranqui, el boleto es de ${bill}')
    elif edad <= 18:
        bill = 7
        #print(f'Pasa tranqui, el boleto es de ${bill}')
    else:
        bill = 12
        #print(f'Pasa tranqui, el boleto es de ${bill}')
    
    want_photo = input('Queres una foto por $3 mas? Y o N\n')
    if want_photo == 'Y':
        bill += 3
    
    print(f'La cuenta es de {bill}')

else: # Es importante ponerle el ":" para terminar
    print('Sorry, no podes subir')