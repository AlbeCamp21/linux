#!/usr/bin/env python3

mi_conjunto = {1, 2, 3}
print(mi_conjunto)  # {1, 2, 3}
print(type(mi_conjunto))  # <class 'set'> 


mi_conjunto.add(8)  # No siempre agrega al último, python decide la manera más óptima
mi_conjunto.update({4, 5, 6, 7, 9, 10, 1.5})  # Igual que "add", pero para más de un elemento


mi_conjunto.remove(3)  # Para eliminar el elemento del set, si no hay dicho elemento lanza error
mi_conjunto.discard(50)  # Igual para eliminar, en caso que no haya NO lanza error


conjunto_1 = {1, 2, 3, 4, 5}
conjunto_2 = {2, 4, 5, 7, 6}
conjunto_interseccion = conjunto_1.intersection(conjunto_2)  # Intersección entre conjuntos
print(conjunto_interseccion)  # {2, 4, 5}


conjunto_1 = {1, 2, 3, 4, 5}
conjunto_2 = {2, 4, 5, 7, 6}
conjunto_union = conjunto_1.union(conjunto_2)  # Unión entre conjuntos
print(conjunto_union)  # {1, 2, 3, 4, 5, 6, 7} No confiarse en el ordenamiento


conjunto_1 = {1, 2, 3}
conjunto_2 = {2, 4, 1, 5, 7, 6, 3}
es_subconjunto = conjunto_1.issubset(conjunto_2)  # ¿Conjunto1 es subconjunto de Conjunto2?
print(es_subconjunto)  # True
conjunto_1 = {"Albe", "Camp"}
conjunto_2 = {"Albe", "AlbeCamp", "Zoey"}
es_subconjunto = conjunto_1.issubset(conjunto_2)
print(es_subconjunto)  # False


mi_lista = [1, 5, 4, 8, 4, 3, 2, 4, 6, 5, 7, 9, 1, 0, 2, 5, 4]
no_repeat = set(mi_lista)  # Casting, de "list" a "set"
print(no_repeat)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
to_list = list(no_repeat)  # Volviéndolo "list"
print(to_list)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


mi_conjunto = set(range(10000))
print(1234 in mi_conjunto)  # Comprobar si un elemento está en un conjunto, True


users_facebook = {"Albe", "Camp", "Felpo", "Zoey"}
user_x = {"Albe", "Felpo", "Memento"}
users_only_facebook = users_facebook.difference(user_x)  # Usuarios que están en Facebook y no en X
users_only_x = user_x.difference(users_facebook)  # Usuarios que están en X y no en Facebook
print(users_only_facebook)  # {'Camp', 'Zoey'}
print(users_only_x)  # {'Memento'}