#!/usr/bin/env python3

class Persona:

    def __init__(self, nombre, edad):  # Persona.__init__(albe, nombre, edad)
        self.nombre = nombre  # albe.nombre = "Albe"
        self.edad = edad  # albe.edad = 37

    def saludo(self):
        print(f"Hola, soy {self.nombre}, con edad de {self.edad} años")
        

albe = Persona("Albe", 37)
albe.saludo()

#----------------------------------------------------------------

class Calculadora:

    def __init__(self, numero):  # Calculadora.__init__(calc, numero)
        self.numero = numero  # calc.numero = 5

    def suma(self, otro_numero):  # calculadora.suma(calc, otro_numero)
        return self.numero + otro_numero  # calc.numero + 8 = 5 + 8

    def doble_suma(self, num1, num2):  # calculadora.doble_suma(calc, 2, 9)
        return self.suma(num1) + self.suma(num2)

calc = Calculadora(5)
print(calc.suma(8))
print(calc.doble_suma(2, 9))