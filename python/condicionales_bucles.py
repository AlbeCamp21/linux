#!/usr/bin/env python3


# else del bucle for
for i in range(10):
    if i == 10:
        break
else:
    print("Bucle for concluido exitosamente")  # Cuando se ejecuta el "break", se activa el "else"


# else del bucle while
i=0
while i<16:
    if i == 10:
        print("Salimos antes de tiempo del bucle while")
        break
    i += 1
else:
    print("El bucle while terminó correctamente")


# operador ternario
edad = 2
mensaje = "Eres mayor de edad" if edad >=18 else "Eres menor de edad"
print(mensaje)


# condicional con lista
mi_lista = [1, 4, 24, 5, 7, 18, 6]
if 4 in mi_lista:
    print("El número está en la lista")
else:
    print("No está en la lista")


names = ["Albe", "AlbeCamp", "Camp"]
for name in names:
    print(f"El nombre es: {name}")
for i,nombre in enumerate(names):  # enumerate devuelve tuplas (clave, valor)
    print(f"Nombre {i+1}°: {nombre}")


frutas = {"manzana" : 1, "pera" : 4, "mango": 9}
for fruta, cantidad in frutas.items():
    print(f"Hay {cantidad} cantidades de la fruta {fruta}")


for i in range(10):
    print(i)
    if i == 5:
        break
for i in range(10):
    if i == 5:
        continue
    print(i)


my_list = [[1, 4, 5], [2, 6, 8], [9, 4, 1]]
for element in my_list:
    print(f"\n[+] Vamos a desglosar la lista {element}:\n")
    for element_in_list in element:
        print(element_in_list)


odd_list = [1, 3, 5, 7, 9]
cuadrado = [i**2 for i in odd_list]
print(cuadrado)


i = 0
while i < 5:
    print(i)
    i += 1
