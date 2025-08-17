#!/usr/bin/env python3

mi_diccionario = {"nombre":"Albe", "edad":54, "pais": "Corea del Norte"}
print(type(mi_diccionario))  # <class 'dict'>
print(mi_diccionario)  # {'nombre': 'Albe', 'edad': 54, 'pais': 'Corea del Norte'}
print(len(mi_diccionario))  # 3


# Modificando valor de una clave
mi_diccionario = {"nombre":"Albe", "edad":54, "pais": "Corea del Norte"}
print(mi_diccionario["edad"])  # 54
mi_diccionario["nombre"] = "Felpo"
print(mi_diccionario["nombre"])  # Felpo
print(mi_diccionario)  # {'nombre': 'Felpo', 'edad': 54, 'pais': 'Corea del Norte'}


# Agregando nuevos valores
mi_diccionario = {"nombre":"Albe", "edad":54, "pais": "Corea del Norte"}
mi_diccionario["profesion"] = "student"
print(mi_diccionario)  # {'nombre': 'Albe', 'edad': 54, 'pais': 'Corea del Norte', 'profesion': 'student'}


# Eliminando un clave-valor
mi_diccionario = {"nombre":"Albe", "edad":54, "pais": "Corea del Norte"}
del mi_diccionario["edad"]
print(mi_diccionario)  # {'nombre': 'Albe', 'pais': 'Corea del Norte'}


# Comprobando si una clave está en un diccionario
mi_diccionario = {"nombre":"Albe", "edad":54, "pais": "Corea del Norte"}
if "pais" in mi_diccionario:
    print("Esta clave está en el diccionario")


# Imprimir todos los key-value de un diccionario
mi_diccionario = {"nombre":"Albe", "edad":54, "pais": "Corea del Norte"}
for key, value in mi_diccionario.items():
    print(f"Para la clave {key} tenemos el valor {value}")


# Vaciar un diccionario
mi_diccionario = {"nombre":"Albe", "edad":54, "pais": "Corea del Norte"}
print(mi_diccionario.clear())  # None
mi_diccionario["nuevo_valor"] = "New"
print(mi_diccionario)  # {'nuevo_valor': 'New'}


# Crear diccionarios con for
cuadrados = {x+1 : (x+1)**2 for x in range(6)}
print(cuadrados)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
print(cuadrados[5])  # 25


# Obtener key y values
mi_diccionario = {"nombre":"Albe", "edad":54, "pais": "Corea del Norte", 12:144}
print(mi_diccionario.keys())  # dict_keys(['nombre', 'edad', 'pais', 12])
print(mi_diccionario.values())  # dict_values(['Albe', 54, 'Corea del Norte', 144])


# Función "get"
mi_diccionario = {"nombre":"Albe", "edad":54, "pais": "Corea del Norte"}
# "get" es como condicional, si no encuentra la key, imprime el segundo argumento
print(mi_diccionario.get("nombre", "Key no encontrada"))  # "Albe"


# Agregar un diccionario a otro
diccionario1 = {"nombre":"Albe", "edad":54, "pais": "Corea del Norte"}
diccionario2 = {"direccion": "Av. Street", 9:"81"}
diccionario1.update(diccionario2)  # Añade los key-value de diccionario2 a diccionario1
print(diccionario1)  # {'nombre': 'Albe', 'edad': 54, 'pais': 'Corea del Norte', 'direccion': 'Av. Street', 9: '81'}


# Diccionario dentro de diccionario
mi_diccionario = {
    "nombre": "Albe",
    "hobbies": {"primero": "música", "segundo": "juegos"},
    "edad": 54
}
print(mi_diccionario)  # {'nombre': 'Albe', 'hobbies': {'primero': 'música', 'segundo': 'juegos'}, 'edad': 54}
print(mi_diccionario["hobbies"]["segundo"])  # juegos
