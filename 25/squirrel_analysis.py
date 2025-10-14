import pandas


# Leer el archivo CSV
data = pandas.read_csv('squirrel_data.csv')

# Agarrar la columna que me interesa
fur_column = data['Primary Fur Color']
fur_list = data['Primary Fur Color'].to_list()

# Extraer los valores unicos
fur_unique = fur_column.unique()

# Extraer los valores unicos LISTA
# fur_unique_list = fur_column.unique().tolist()

gray_count = 0
black_count = 0
cinnamon_count = 0

# for value in fur_list:
#     if value == 'Gray':
#         gray_count += 1
#     elif value == 'Black':
#         black_count += 1
#     elif value == 'Cinnamon':
#         cinnamon_count += 1

hola = fur_column.value_counts()
# Crear un CSV que tenga la cantidad de ardillas de cada color

# print(gray_count)
# print(black_count)
# print(cinnamon_count)

main_data = pandas.DataFrame(hola)
print(main_data)

main_data.to_csv('./main_squirrel.csv')
# for value in fur_unique:
#     print(value)