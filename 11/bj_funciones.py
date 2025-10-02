from bj_data import mazo_numeros,valores, jugadores, mazo_numeros2
from art import blackjack, playing, win, lose, draw
import random
pozo = []


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

    mazo_numeros = mazo_numeros2


def imprimir_status(jugador1,jugador2):
    print(f"Tu mano es {jugadores[jugador1]['mano']} y la suma es {jugadores[jugador1]['mano']}")
    print(f"Tu mano es {jugadores[jugador2]['mano']} y la suma es {jugadores[jugador2]['mano']}")

        