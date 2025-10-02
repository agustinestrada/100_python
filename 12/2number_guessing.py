import random
guessing = """
  _______  __    __   _______     _______.     _______. __  .__   __.   _______      _______      ___      .___  ___.  _______ 
 /  _____||  |  |  | |   ____|   /       |    /       ||  | |  \ |  |  /  _____|    /  _____|    /   \     |   \/   | |   ____|
|  |  __  |  |  |  | |  |__     |   (----`   |   (----`|  | |   \|  | |  |  __     |  |  __     /  ^  \    |  \  /  | |  |__   
|  | |_ | |  |  |  | |   __|     \   \        \   \    |  | |  . `  | |  | |_ |    |  | |_ |   /  /_\  \   |  |\/|  | |   __|  
|  |__| | |  `--'  | |  |____.----)   |   .----)   |   |  | |  |\   | |  |__| |    |  |__| |  /  _____  \  |  |  |  | |  |____ 
 \______|  \______/  |_______|_______/    |_______/    |__| |__| \__|  \______|     \______| /__/     \__\ |__|  |__| |_______|
                                                                                                                               
"""


# print('Welcome to the Number Guessing Game!')
print(guessing)
print("I'm thinking of a number between 1 and 100")

DIFFICULTY = input('Choose a dificulty. Type "Easy" or "Hard"\nEasy for 10 guesses and Hard for 5 guesses\n').capitalize()
NUMERO_ADIVINANZA = random.randint(1,100)

def juego(dificultad):
    intentos = 0
    acierto = False

    if dificultad == "Easy":
        intentos = 10
    elif dificultad == "Hard":
        intentos = 5

    while intentos > 0 and not acierto:
        eleccion = int(input('Por favor elija un numero del 1 al 100\n'))
        if eleccion == NUMERO_ADIVINANZA:
            print(f'Ganaste el numero era {NUMERO_ADIVINANZA}')
            acierto = True
        elif eleccion > NUMERO_ADIVINANZA:
            print('Demasiado alto')
            intentos -= 1
            print(f'Te quedan {intentos} intentos')
        elif eleccion < NUMERO_ADIVINANZA:
            print('Demasiado bajo')
            intentos -= 1
            print(f'Te quedan {intentos} intentos')
    
    if intentos == 0:
        print(f'Perdiste, se te acabaron los intentos :(\nEl numero era {NUMERO_ADIVINANZA}')

juego(DIFFICULTY)