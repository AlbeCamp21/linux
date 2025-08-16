#!/usr/bin/env python3

puertos_tcp = [21, 22, 25, 80, 443, 8000, 445, 69]
puertos_tcp.append(1337)
print(puertos_tcp)
print(len(puertos_tcp))
for puerto in puertos_tcp:
    print(f"Este es el puerto {puerto}")
puertos_tcp.sort()  # Ordena de menor a mayor
print(puertos_tcp)


cve_list = ['CVE-2023-1435', 'CVE-2022-45761', 'CVE-2023-7863']
print(cve_list)
cve_list.remove('CVE-2023-7863')  # Quita el elemento de la lista (si hay varios, entonces solamente el primero)
print(cve_list)


attacks = ['Phishing', 'DDoS', 'SQL Injection', 'Man In The Middle', 'XXS']
print(attacks)
attacks.reverse()  # Invierte elementos en el mismo array
print(attacks)


attacks = ['Phishing', 'DDoS', 'SQL Injection', 'Man In The Middle', 'XXS']
another_attacks_list = attacks[:3]  # ['Phishing', 'DDoS', 'SQL Injection'
last_attack = attacks[-1]  # 'XXS'
second_last_attack = attacks[-2]  # 'Man In The Middle'
print(another_attacks_list)


attacks = ['Phishing', 'DDoS', 'SQL Injection', 'Man In The Middle', 'XXS']
for i, attack in enumerate(attacks):  # "enumerate" devuelve tuplas (clave, valor)
    print(f"Para la posición {i+1} tenemos el ataque {attack}")


attacks = ['Phishing', 'DDoS', 'SQL Injection', 'Man In The Middle', 'XXS']
attacks_uppercase = [attack.upper() for attack in attacks]
print(attacks_uppercase)


names = ["Albe", "Camp", "AlbeCamp", "Felpo"]
edades = [54, 21, 49, 5]
for name, edad in zip(names, edades):  # "zip" itera a la vez para los arrays, unidad por unidad
    print(f"{name} tiene {edad} años")


names = ["Albe", "Camp", "AlbeCamp", "Felpo"]
del names[2]  # Eliminación según el indice
print(names)  # ["Albe", "Camp", "Felpo"]


names = ["Albe", "Camp", "AlbeCamp", "Felpo"]
names.clear()  # Borra todos los elementos del array
print(names)  # []


names = ["Albe", "Camp", "AlbeCamp", "Felpo"]
deleted_user = names.pop()  # Extrae el último elemento del array (también se le puede asignar un índice)
#  "deleted_user ahora almacena "Felp"
#  names = ["Albe", "Camp", "AlbeCamp"]
print(f"El usuario {deleted_user} ha sido eliminado")


names = ["Albe", "Camp", "AlbeCamp", "Felpo"]
names[2] = "Masmemoe"
#  names = ["Albe", "Camp", "Masmemoe", "Felpo"]


names = ["Albe", "Camp", "AlbeCamp", "Felpo"]
names.insert(2, "Masmemoe")
#  #  names = ["Albe", "Camp", "Masmemoe", "AlbeCamp", "Felpo"]


names = ["Albe", "Camp", "AlbeCamp", "Felpo"]
more_names = ["Masmemoe", "Fedora", "Zoey"]
names.extend(more_names)  # añade los elementos de "more_names" a "names"
print(names)  # ['Albe', 'Camp', 'AlbeCamp', 'Felpo', 'Masmemoe', 'Fedora', 'Zoey']