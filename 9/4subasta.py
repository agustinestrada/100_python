from logo import logo2
print(logo2)

participantes = {}

hay_mas_participantes = True
n_participante = 1
participante_ganador = {
    'nombre':'nombre',
    'puja': 0
}

# Recopilacion de participantes y pujas
while hay_mas_participantes:
    participante = input('Introducir el nombre del participante\n')
    puja = input('Introduzca su oferta\n')
    
    participantes[n_participante] = {participante : puja}
    
    n_participante += 1
    
    # Evaluacion si hay mas oferentes
    hay_personas = input('Hay mas personas que quieran ofrecer? Y o N\n')
    
    if hay_personas == 'N':
        hay_mas_participantes = False


# Imprimir si hay un unico participante y ganador
if len(participantes) == 1:
    datos = participantes[1]
    nombre = ''
    puja = ''
    for nombre, puja in datos.items():
        nombre = nombre
        puja = puja
    
    participante_ganador = participantes
    print(f'El participante ganador es {nombre} con la apuesta de {puja}')
    exit()

for parti in participantes:
    datos = participantes[parti]
    nombre = ''
    puja = 0

    for nom, puj in datos.items():
        if int(puj) > int(participante_ganador['puja']):
            participante_ganador = { 'nombre': nom, 'puja': puj}

print(f'El participante ganador es {participante_ganador["nombre"]} con la apuesta de {participante_ganador["puja"]}')
print('\n'*3)
print(max(participantes))
