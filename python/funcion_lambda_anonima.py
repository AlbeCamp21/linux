#!/usr/bin/env python3

mi_funcion = lambda: "Hola soy albe"
print(mi_funcion())

cuadrado = lambda x: x**2
print(cuadrado(6))

suma = lambda x ,y: x + y
print(suma(5, 6))

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cuadrados = list(map(lambda x: x**2, numeros))  # map itera una función (1° argumento) a una lista (2° argumento)
print(cuadrados)
pares = list(filter(lambda x: x % 2 == 0, numeros))  # filter obtiene los valores que devuelven true
print(pares)

from functools import reduce
numeros2 = [1, 2, 3, 4, 5]
producto = reduce(lambda x, y: x*y, numeros2)  # reduce reutiliza los resultados (los outputs se vuelven inputs)
print(producto)  # 120