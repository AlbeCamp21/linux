#!/usr/bin/env python3

def saludo(nombre):
    print(f"\nHola {nombre}")
saludo("Albe")


def suma(x, y):
    return x + y
resultado = suma(2, 8)
print(f"\nLa suma de los números es: {resultado} o {suma(2, 8)}")


def mi_funcion():
    variable_local = "\nSoy una variable local\n"
    print(variable_local)
mi_funcion()


variable1 = "Soy global"
def mi_funcion2():
    variable1 = "Soy local"
    print(variable1)
mi_funcion2()  # Imprime "Soy local"
print(variable1)  # Imprime "Soy global"


print(" ")


variable2 = "Soy global"
def mi_funcion2():
    global variable2  # hace accesible las variables para modificarlas desde la función
    variable2 = "Soy global y he sido modificado"
    print(variable2)
mi_funcion2()  # Imprime "Soy global y he sido modificado"
print(variable2)  # Imprime "Soy global y he sido modificado"