#!/usr/bin/env python3

def mi_decorador(funcion):  # Función de orden superior
    def envoltura():
        print("Estoy saludando en la envoltura del decorador antes de llamar a la función")
        funcion()  # Llamada a la función original
        print("Estoy saludando en la envoltura del decorador después de llamar a la función")
    return envoltura

@mi_decorador
def saludo():
    print("Hola, estoy saludando dentro de la función")

saludo()
# Estoy saludando en la envoltura del decorador antes de llamar a la función
# Hola, estoy saludando dentro de la función
# Estoy saludando en la envoltura del decorador después de llamar a la función

#----------------------------------------------------------------

class Persona:

    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def edad(self):  # Getter
        return self._edad
    
    @edad.setter  # Setter, siempre lleva el mismo nombre del getter
    def edad(self, valor):
        if valor >= 0:
            self._edad = valor
        else:
            raise ValueError("[!] La edad no puede ser un número negativo")

albe = Persona("Albe", 34)
albe.edad = 4  # Setter
print(albe.edad)  # Getter
# Ahora se puede acceder y modificar el atributo protegido "edad" de manera adecuada

#----------------------------------------------------------------

import time

def cronometro(funcion):
    def envoltura(num):  # Si la función principal requiere argumentos, entonces a "envoltura" también se le pone esos argumentos 
        inicio = time.time()
        funcion(num)
        final = time.time()
        print(f"Tiempo total transcurrido en la función {funcion.__name__}: {final-inicio}")
    return envoltura

@cronometro
def pausa_corta(num):
    time.sleep(num)

@cronometro
def pausa_larga(num):
    time.sleep(num)

pausa_corta(2)  # Tiempo total transcurrido en la función pausa_corta: 2.0001323223114014
pausa_larga(3)  # Tiempo total transcurrido en la función pausa_larga: 3.0001437664031982

#----------------------------------------------------------------
# VERSION MÁS "ESCALABLE" HACIENDO USO DE args Y kwargs

import time

def cronometro(funcion):
    def envoltura(*args, **kwargs):  # Si la función principal requiere argumentos, entonces a "envoltura" también se le pone esos argumentos 
        inicio = time.time()
        funcion()
        final = time.time()
        print(f"Tiempo total transcurrido en la función {funcion.__name__}: {final-inicio}")
        if args:  # si hay algo en "args" (si se le pasó una tupla)
            print(args)
        if kwargs:  # si hay algo en "kwargs" (si se le pasó un diccionario / clave-valor)
            print(kwargs)
    return envoltura

@cronometro
def pausa_corta(*args, **kwargs):
    time.sleep(1)

@cronometro
def pausa_larga(*args, **kwargs):
    time.sleep(2)

pausa_corta(2, 3, 4, 8, nombre="Albe", edad=12)
# Tiempo total transcurrido en la función pausa_corta: 1.000478744506836
# (2, 3, 4, 8)
# {'nombre': 'Albe', 'edad': 12}
pausa_larga()
# Tiempo total transcurrido en la función pausa_larga: 2.000276803970337