#!/usr/bin/env python3

example = (1, "test", 3, 4, 5, [1, 2])
print(example)
print(example[1:3])  # Los índices funcionan de la misma manera que las listas
# example[2] = 34  # Error ya que son inmutables
for element in example:
    print(element)


# No se puede aplicar funciones tipo: append, extend, pop, etc.


mi_tupla = (1, 2, 3, 4)
a, b ,c, d = mi_tupla
print(a)  # 1
print(b)  # 2
print(c)  # 3
print(d)  # 4


mi_primera_tupla = (1, 2, 3, 4)
mi_segunda_tupla = (5, 6, 7, 8, 9)
mi_tercera_tupla = mi_primera_tupla + mi_segunda_tupla
print(mi_tercera_tupla)  # (1, 2, 3, 4, 5, 6, 7, 8, 9)


mi_primera_tupla = (1, 2, 3, 4)
mi_tercera_tupla = mi_primera_tupla*3
print(mi_tercera_tupla)  # (1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)


mi_tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
numeros_pares = tuple(i for i in mi_tupla if i % 2 == 0)
print(numeros_pares)  # (2, 4, 6, 8, 10)


db1_credential = ("Albe", "Albe123")
try:
    db1_credential[0] = "Camp"
except TypeError:
    print("No es posible manipular los elementos de una tupla")