import random
from art import logo
from game_data import data
from pprint import pprint

ids = []

def agregar_id():
	for i in range(0,len(data)):
		data[i]['id'] = i

agregar_id()

for person in data:
	ids.append(person['id'])

def empezar():
	primera_opcion = random.choice(ids)
	ids.remove(primera_opcion)
	segunda_opcion = random.choice(ids)
	ids.remove(segunda_opcion)
	anterior = segunda_opcion
	return primera_opcion,segunda_opcion,anterior

primera_opcion, segunda_opcion, anterior = empezar()

print(primera_opcion,segunda_opcion,anterior)

# if ids == []:
# 	print('No hay mas personas para comparar\nAdios')
# 	exit()