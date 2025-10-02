from bj_data import jugadores
from bj_funciones import calcular_mano,dar_carta,repartir, reiniciar_juego
from art import lose,win,draw,blackjack

io = 'Agus'
voi = 'la_casa'
jugar = True
mi_turno = True
su_turno = True

print(blackjack)

def game_over(quien):
    if jugadores[quien]['suma'] > 21:
        global mi_turno, su_turno, jugar
        print(lose)
        mi_turno = False
        su_turno = False
        jugar = False

while jugar:
    repartir(io,voi)

    while mi_turno:
        if jugadores[io]['suma'] == 21:
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
            su_turno = False
            print(f"Tus {jugadores[io]['suma']} vs sus {jugadores[voi]['suma']}")
            jugar
        elif jugadores[voi]['suma'] == jugadores[io]['suma'] and su_turno:
            print(draw)
            su_turno = False
        
    otra_vez = input('Queres seguir jugando? Y o N\n')

    if otra_vez == 'N':
        jugar = False
        print('BYE')
        exit()

    reiniciar_juego(io,voi)
    mi_turno = True
    jugar = True
    su_turno = True



