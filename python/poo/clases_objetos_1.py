#!/usr/bin/env python3

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludo(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años"

albe = Persona("Albe", 54)
felpo = Persona("Felpo", 18)
print(felpo.saludo())
print(albe.saludo())

#----------------------------------------------------------------

class Animal:

    def __init__(self, nombre, animal):
        self.nombre = nombre
        self.animal = animal
        
    def descripcion(self):
        print(f"{self.nombre} es un {self.animal}")    
        
gato = Animal("Michi", "Gato")
perro = Animal("Newton", "Perro")
gato.descripcion()
perro.descripcion()

#----------------------------------------------------------------

class CuentaBancaria:

    def __init__(self, cuenta, nombre, dinero=0):
        self.cuenta = cuenta
        self.nombre = nombre
        self.dinero = dinero

    def depositar_dinero(self, dinero):
        self.dinero += dinero
        return f"\n[+] [{self.nombre}] Se han depositado {dinero} dólares\n[+] [{self.nombre}] Tu monto actual es de {self.dinero} dólares"
    
    def retirar_dinero(self, dinero):
        if dinero > self.dinero:
            return f"\n[!] [{self.nombre}] Operación denegada: Fondos insuficientes"
        else:
            self.dinero -= dinero
            return f"\n[+] [{self.nombre}] Se han retirado {dinero} dólares\n[+] [{self.nombre}] Tu monto actual es de {self.dinero} dólares"


albe = CuentaBancaria("148679", "Albe Camp", 2000)
zoey = CuentaBancaria("654879", "Zoey Hunt")
print(albe.depositar_dinero(500))
print(albe.retirar_dinero(600))
print(albe.retirar_dinero(2000))
print(zoey.depositar_dinero(100))