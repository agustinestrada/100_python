persona = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Buenos Aires"
}

persona2 = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Buenos Aires"
}

# Ejercicio 1 - Crear y Acceder
# 👉 Imprime el nombre y la edad por separado.

# 🔹 Ejercicio 2 – Agregar y modificar
# 	1.	Agrega una clave "profesion" con el valor "programador".
# 	2.	Cambia la edad a 26.

# 	3.	Imprime el diccionario actualizado.
# 🔹 Ejercicio 3 – Eliminar
# Elimina la clave "ciudad" del diccionario e imprime el resultado.

# 🔹 Ejercicio 4 – Recorrer diccionario
# Dado este diccionario:
colores = {
    "rojo": "#FF0000",
    "verde": "#00FF00",
    "azul": "#0000FF"
}
# 👉 Recorre el diccionario e imprime:
# El color rojo tiene el código #FF0000 (y así con todos).

# 🔹 Ejercicio 5 – Contar palabras
# Dado este texto:

texto = "python es genial y python es divertido"

# 👉 Usa un diccionario para contar cuántas veces aparece cada palabra.
# Resultado esperado:


#E1
print(persona["nombre"])
print(persona['edad'])

#E2
persona['profesion'] = 'programador'
persona["edad"] = 26
print(persona)

#E3
# Eliminar directamente es con "del" pero si quiero eliminar y poder quedarme con el valor es .pop('clave)

del persona2["ciudad"]
edad_persona_2 = persona2.pop('edad')

print(f'La edad de la persona 2 era de {edad_persona_2}')
print(persona2)

#E4
# for color in colores:
#     # Para iterar y poner el nombre del KEY es entre llaves sin el value
#     print(f'El color {color} tiene el codigo {colores[color]}')

# for key, value in diccionario.items:
#     # Agregando el .items al diccionario y usando 2 parametros el primero se transforma en key y el segundo en value
#     print(f'El color {color} tiene el codigo {colores[color]}')

for nombre, color in colores.items():
    # Es importante que el color.items tenga los () para ejecutar la funcion
    print(f'El color {nombre} tiene el codigo {color}')


#E5

