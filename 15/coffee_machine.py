from data import MENU, coffee_machine, COINS

def eval_ingredientes(bebida):
	"""Esta funcion va a evaluar que la maquina tenga los ingredientes necesarios y restarle las cantidades que la bebida necesita a la maquina"""
	
	water = MENU[bebida]['ingredients']['water']
	# La sentencia .get() es un método de diccionarios en Python.
	# clave → la key que querés buscar en el diccionario.
	# valor_por_defecto (opcional) → lo que devuelve si la clave no existe.
	milk = MENU[bebida]['ingredients'].get('milk',0)
	coffee = MENU[bebida]['ingredients']['coffee']

	if coffee_machine['water'] < water or coffee_machine['milk'] < milk or coffee_machine['coffee'] < coffee:
		print('No tenes suficientes ingredientes')
		cargar_maquina = input('Queres recargar la maquina y hacer el cafe? Y o N').lower()
		if cargar_maquina == 'y':
			recarga()
		else:
			print('Sera otro dia')
			exit()

	coffee_machine['water'] -= water
	coffee_machine['milk'] -= milk
	coffee_machine['coffee'] -= coffee
	return True
		
def ingresar_plata(bebida):
	"""Funcion para agregar plata en la maquina, devuelve False si no alcanza la plata y True si no hay problema"""
	print(f"La bebida cuesta ${MENU[bebida]['cost']}")
	pennys = int(input('Ingrese la cantidad de pennys\n')) * COINS['penny']
	nickels = int(input('Ingrese la cantidad de nickels\n')) * COINS['nickel']
	dimes = int(input('Ingrese la cantidad de dimes\n')) * COINS['dime']
	quarters = int(input('Ingrese la cantidad de quarters\n')) * COINS['quarter']

	plata_total = float((pennys + nickels + dimes + quarters) /100)

	if plata_total < MENU[bebida]['cost']:
		print(f"Falta plata, ingresaste ${plata_total} y se necesita ${MENU[bebida]['cost']}")
		return False
	else:
		return True 

def report():
	"""Nos da un status de la cantidad de ingredientes en la maquina"""
	# for resourse, amount in coffee_machine.items():
	# 	print(f'{resourse}: {amount}')
	for resourse in coffee_machine:
		print(f'{resourse}: {coffee_machine[resourse]}')

def recarga():
	coffee_machine['water'] = 300
	coffee_machine['milk'] = 200
	coffee_machine['coffee'] = 100

def bebida_validada(bebida):
	if bebida in MENU:
		return True
	elif bebida == 'report':
		report()
		return False
	else:
		return False
	
	# Reemplaza a todo lo que esta aca abajo
	# if bebida == "espresso":
	# 	return True
	# elif bebida == "latte":
	# 	return True
	# elif bebida == "cappuccino":
	# 	return True
	# elif bebida == "report":
	# 	report()
	# 	bebida = input('Que bebida quiere? o ingrese "Report" para diagnostico de la maquina\nEspresso, Latte o Cappuccino\n').lower()
	# else:
	# 	return False

cafetera_encendida = True



while cafetera_encendida:
	bebida_elegida = input('Que bebida quiere? o ingrese "Report" para diagnostico de la maquina\nEspresso, Latte o Cappuccino\n').lower()

	bebida_ok = bebida_validada(bebida_elegida)
	
	while not bebida_ok:
		bebida_elegida = input('Que bebida quiere? o ingrese "Report" para diagnostico de la maquina\nEspresso, Latte o Cappuccino\n').lower()
		bebida_ok = bebida_validada(bebida_elegida)
		
	p = ingresar_plata(bebida_elegida)
	

	if p:
		i = eval_ingredientes(bebida_elegida)
		if i:
			print('Aca tenes tu cafe')
	
	otro = input('Queres otro cafe? Y o N\n').lower()

	if otro == 'n':
		print('Sera otro dia')
		cafetera_encendida = False
