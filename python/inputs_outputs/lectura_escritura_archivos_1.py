#!/usr/bin/env python3

# Crear un archivo "example.txt" ("¡Hola mundo!")

# "w": write, reemplaza el contenido con lo que añadamos (borramos todo el contenido, cuidado)
# "a": append, para agregar, acá sobreescribimos
# "r": read, en caso que no exista el archivo, puede generar error

f = open("example_1.txt", 'w')
f.write("¡Hola mundo!")  # crea "example.txt" en caso no exista, y escribe "¡Hola mundo!"
f.close()  # para cerrar

f = open("example_1.txt", 'a')
f.write(", soy Albe")  # ¡Hola mundo!, soy Albe
f.close()

f = open("example_1.txt", 'w')
f.write("Adios")  # Adios
f.close()

#----------------------------------------------------------------
# Otra forma más óptima, python se encarga de cerrar el archivo cada vez, mismos resultados

with open("example_1.txt", 'w') as f:
    f.write("¡Hola mundo!")

with open("example_1.txt", 'a') as f:
    f.write(", soy Albe")

with open("example_1.txt", 'w') as f:
    f.write("Adios")