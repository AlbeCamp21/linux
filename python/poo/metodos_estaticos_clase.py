#!/usr/bin/env python3

class Calculadora:

    @staticmethod
    def suma(num1, num2):
        return num1 + num2

    @staticmethod
    def resta(num1, num2):
        return num1 - num2
    
    @staticmethod
    def multiplicacion(num1, num2):
        return num1 * num2
    
    @staticmethod
    def division(num1, num2):
        return num1 / num2 if num2 != 0 else "\n[!] Error: No se puede dividir un número entre cero"

print(Calculadora.suma(2, 8))
print(Calculadora.resta(8, 4))
print(Calculadora.multiplicacion(2, 5))
print(Calculadora.division(5, 0))

#----------------------------------------------------------------

class Automovil:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @classmethod
    def deportivos(cls, marca):
        return cls(marca, "Deportivo")
    
    @classmethod
    def sean(cls, marca):
        return cls(marca, "Sean")

    def __str__(self):
        return f"\n[+] La marca {self.marca} es un modelo {self.modelo}"

vehiculo_uno = print(Automovil.deportivos("Ferrari"))  # Automovil("Ferrari", "Deportivo")
vehiculo_dos = print(Automovil.sean("Toyota"))  # Automovil("Toyota", "Sean")

#----------------------------------------------------------------

class Estudiantes:
    
    estudiantes = []

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        Estudiantes.estudiantes.append(self)

    @staticmethod
    def es_mayor_de_edad(edad):
        return edad >= 18

    @classmethod
    def crear_estudiante(cls, nombre, edad):
        if cls.es_mayor_de_edad(edad):
            return cls(nombre, edad)
        else:
            print(f"\n[!] Error: El estudiante {nombre} es menor de edad\n")

    @staticmethod
    def mostrar_estudiantes():
        for i, estudiante in enumerate(Estudiantes.estudiantes):
            print(f"[+] Estudiante {i+1}°: {estudiante.nombre}")

Estudiantes.crear_estudiante("Albe", 54)
Estudiantes.crear_estudiante("Felpo", 18)
Estudiantes.crear_estudiante("Camp", 16)
Estudiantes.crear_estudiante("Zoey", 24)
Estudiantes.mostrar_estudiantes()