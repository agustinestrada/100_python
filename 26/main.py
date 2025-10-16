with open('file1.txt') as file:
    data1 = file.readlines()

with open('file2.txt') as file:
    data2 = file.readlines()

da1_2 = [w.replace('\n','') for w in data1]
da2_2 = [w.replace('\n','') for w in data2]

lista1 = [int(nu) for nu in da1_2]
lista2 = [int(nu) for nu in da2_2]

lista_conjunta = []

# for i in lista1:
#     if lista2.count(i):
#         lista_conjunta.append(i)

lista_conjunta = [i for i in lista1 if lista2.count(i)]

print(lista_conjunta)