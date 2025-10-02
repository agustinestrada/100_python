edad = int(input('Escribir su edad\n'))

def life_in_weeks(edades):
    anos_restantes = 90 - edades
    semanas_restantes = anos_restantes*52
    print(f'Te quedan {semanas_restantes} semanas')

life_in_weeks(edad)
