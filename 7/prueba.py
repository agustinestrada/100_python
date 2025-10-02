n1 = input('Ingresa el primer nombre\n').lower()
n2 = input('Ingresa el segundo nombre\n').lower()
nombres = n1+n2
t = 'true'
l = 'love'

tru = []
lov = []
porcentaje = ''

for number in range(0,4):
    tru.append(nombres.count(t[number]))
    lov.append(nombres.count(l[number]))

porcentaje = str(sum(tru)) + str(sum(lov))

print(porcentaje)