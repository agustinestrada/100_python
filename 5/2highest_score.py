
scores = [19, 93, 4, 39, 56, 45, 64, 24, 50, 61, 56, 10, 67, 12, 81, 27, 25, 57, 75, 67, 14, 81, 38, 13, 68, 40, 14, 5, 46, 64, 67, 88, 89, 2, 55, 87, 49, 28, 19, 16, 23, 27, 48, 98, 89, 17, 13, 9, 56]

# SUMA
# suma_manual = 0

# for score in scores:
#     suma_manual += score

# suma_automatica = sum(scores)

# print(suma_manual)
# print(suma_automatica)

# Encontrar el MAXIMO

maximo = 0

for score in scores:
    if score > maximo:
        maximo = score
        
print(maximo)