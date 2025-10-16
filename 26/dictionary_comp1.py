sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
lista1 = sentence.split()
result = { i:len(i) for i in lista1}
print(result)