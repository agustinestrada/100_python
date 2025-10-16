from random import randint as r
nombres = ["Sofia", "Agustin", "Martina", "Lucas", "Valentina", "Tomas", "Camila", "Mateo"]

nombres_scores = { nom:int(r(1,100)) for nom in nombres }
nombres_aprovados = { llave:valor for (llave,valor) in nombres_scores.items() if nombres_scores[llave] > 60}

print(nombres_scores)
print(nombres_aprovados)