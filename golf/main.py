import pandas

# sexo = input('Por favor indice su sexo, C o D')

data = pandas.read_csv('data.csv')
club_columna = data['Club']
cancha_columna = data['Cancha']
tee_columna = data['Tee']


# Unicos
clubes = club_columna.unique()
canchas = cancha_columna.unique()
tees = tee_columna.unique()





club = input(f'Que club quiere jugar\n{clubes}\n\n').title()
cancha = data[data['Club'] == club]




# club = input(f'Que tee quiere jugar\n{clubes}').title()


