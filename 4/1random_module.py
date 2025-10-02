import random

# Para generar Random INTEGERS. Ambos Inclusive
random_number = random.randint(1,2)
print(random_number)

# # Para generar random FLOATS entre [0; 1)
random_0_to_1 = random.random()
print(random_0_to_1)

# Para generar random FLOATS entre dos numeros a eleccion. Ambos Inclusive [x;y]
random_floats = random.uniform(10,14)
print(random_floats)