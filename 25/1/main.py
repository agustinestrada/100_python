import pandas

data = pandas.read_csv('clima.csv')

# print(data['condicion'])

# data_to_dict = data.to_dict()

# print(data_to_dict)

# Calcular el promedio de la temperatura

# cantidad_de_filas = 10

# MEAN se usa para sacar promedios, es como AVERAGE
# min_avg = data['minima'].mean()
# max_avg = data['maxima'].mean()

# MAX y MIN devuelven los valores maximos y minimos de una Serie de Pandas
# max_tem = data['maxima'].max()
# min_tem = data['minima'].min()

# print(f'El promedio de minima va a ser: {min_avg} y de maxima: {max_avg}\nLa temperatura maxima de la semana es: {max_tem}\nLa temperatura minima de la semana es: {min_tem}')


print(data[data.minima == data.minima.min()])