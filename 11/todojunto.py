import random
pozo = []
io = 'Agus'
voi = 'la_casa'
jugar = True
mi_turno = True
su_turno = True

blackjack = """
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                       _/ |                
                      |__/           
"""

win = """
 __   __           __        ___       _ 
 \ \ / /__  _   _  \ \      / (_)_ __ | |
  \ V / _ \| | | |  \ \ /\ / /| | '_ \| |
   | | (_) | |_| |   \ V  V / | | | | |_|
   |_|\___/ \__,_|    \_/\_/  |_|_| |_(_)
"""

lose = """
 __   __            _                   _ 
 \ \ / /__  _   _  | |    ___  ___  ___| |
  \ V / _ \| | | | | |   / _ \/ __|/ _ \ |
   | | (_) | |_| | | |__| (_) \__ \  __/_|
   |_|\___/ \__,_| |_____\___/|___/\___(_)
"""

draw = """
  ____  ____      ___        ___ _ 
 |  _ \|  _ \    / \ \      / / | |
 | | | | |_) |  / _ \ \ /\ / /| | |
 | |_| |  _ <  / ___ \ V  V / |_|_|
 |____/|_| \_\/_/   \_\_/\_/  (_|_)
"""

# Generar lista de números del 1 al 13, cada uno repetido 4 veces
mazo_numeros = ["As", "As", "As", "As", 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K"]
mazo_numeros2 = ["As", "As", "As", "As", 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K"]

valores = {
    '1': 1,
    'As': 11,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
}

jugadores = {
    'Agus': {
        'mano': [],
        'suma': 0,
        'ases': 0,
    },
    'la_casa': {
        'mano': [],
        'suma': 0,
        'ases': 0
    }
}


def dar_carta(quien):
    carta = random.choice(mazo_numeros)
    jugadores[quien]['mano'].append(carta)
    mazo_numeros.remove(carta)
    pozo.append(carta)
    if carta == 'As':
        jugadores[quien]['ases'] += 1

def calcular_simple(quien):
    jugadores[quien]['suma'] = 0
    for carta in jugadores[quien]['mano']:
        for valor in valores:
            if str(carta) == valor:
                jugadores[quien]['suma'] += valores[valor]
    
def calcular_mano(quien):
    calcular_simple(quien)

    # Entrar en la evaluacion de los Ases
    if jugadores[quien]['ases'] > 0:
        posicion_ases = []
        pa = 0

        # Encontrar los Ases
        for ind in jugadores[quien]['mano']:
            if ind == 'As':
                posicion_ases.append(jugadores[quien]['mano'].index(ind,pa))
                pa = jugadores[quien]['mano'].index(ind,pa) + 1
        

        # Reemplazo de ases si la suma supera 21
        for i in posicion_ases:
            if jugadores[quien]['suma'] > 21:
                jugadores[quien]['mano'][i] = 1
                posicion_ases.pop(0)
        
    
        calcular_simple(quien)

    else:
        calcular_simple(quien)

    
    print(f"La mano de {quien} es {jugadores[quien]['mano']} y suma {jugadores[quien]['suma']}")
   
def repartir(jugador1, jugador2):
    dar_carta(jugador1)
    dar_carta(jugador1)
    dar_carta(jugador2)
    jugadores[jugador2]['mano'].append('x')
    calcular_mano(jugador1)
    print(jugadores[jugador2]['mano'])
    jugadores[jugador2]['mano'].remove('x')
        
def reiniciar_juego(jugador1,jugador2):
    print('\n'*100)

    print(blackjack)

    jugadores[jugador1]['mano'] = []
    jugadores[jugador1]['suma'] = 0
    jugadores[jugador1]['ases'] = 0

    jugadores[jugador2]['mano'] = []
    jugadores[jugador2]['suma'] = 0
    jugadores[jugador2]['ases'] = 0

def imprimir_status(jugador1,jugador2):
    print(f"Tu mano es {jugadores[jugador1]['mano']} y la suma es {jugadores[jugador1]['mano']}")
    print(f"Tu mano es {jugadores[jugador2]['mano']} y la suma es {jugadores[jugador2]['mano']}")

def game_over(quien):
    global mi_turno,su_turno
    if jugadores[quien]['suma'] > 21:
        print(lose)
        mi_turno = False
        su_turno = False

# El juego
print(blackjack)


while jugar:
    repartir(io,voi)

    while mi_turno:
        if jugadores[io]['suma'] == 21 and len(jugadores[io]['mano']) == 2:
            print(win,blackjack)
            su_turno = False
            break
        
        else:
            otra_carta = input('Queres otra carta? Y o N\n')
            
            if otra_carta == 'Y':
                dar_carta(io)
                calcular_mano(io)
            
            elif otra_carta == 'N':
                mi_turno = False
            else:
                print('Por favor introduzca una respuesta valida')
                otra_carta
            
            game_over(io)

    while su_turno:
        while jugadores[voi]['suma'] < jugadores[io]['suma']:
            dar_carta(voi)
            calcular_mano(voi)

        if jugadores[voi]['suma'] > 21 and su_turno:
            print(win)
            print(f"Tus {jugadores[io]['suma']} vs sus {jugadores[voi]['suma']}")
            su_turno = False
            jugar = False
        elif jugadores[voi]['suma'] > jugadores[io]['suma'] and su_turno:
            print(lose)
            print(f"Tus {jugadores[io]['suma']} vs sus {jugadores[voi]['suma']}")
            jugar = False
            su_turno = False
        elif jugadores[voi]['suma'] == jugadores[io]['suma'] and su_turno:
            print(draw)
            su_turno = False
            jugar = False
        
    otra_vez = input('Queres seguir jugando? Y o N\n')

    if otra_vez == 'N':
        jugar = False
        print('BYE')
        exit()

    reiniciar_juego(io,voi)
    mazo_numeros = mazo_numeros2
    mi_turno = True
    jugar = True
    su_turno = True
    
