#!/usr/bin/env python3

name = "AlbeCamp"
rol = "lammer"
edad = 54

# s: string, d: entero
print("Hola, mi nombre es %s, soy un %s y tengo la edad de %d" % (name, rol, edad))

print ("---")

print("Hola, soy {}".format(name))
print("Hola, soy {0}, tengo {1} años. Mentira, mi nombre real es {0}".format(name,edad))

print ("---")

print(f"Hola, soy {name}")
print(f"Hola, soy {name}, tengo {edad+100} años. Mentira, mi nombre real es {name + "Albe"}")