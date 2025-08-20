#!/usr/bin/env python3

class Ejemplo:

    def __init__(self):
        # Atributo protegido (1 guión)
        self._atributo_protegido = "Soy un atributo protegido y no deberías verme"
        # Atributo privado (2 guiones)
        self.__atributo_privado = "Soy un atributo privado y no deberías verme"

ejemplo = Ejemplo()
print(ejemplo._atributo_protegido)  # Soy un atributo protegido y no deberías verme
# print(ejemplo.__atributo_privado)  # Error
# Forma adecuada para poder ver un atributo privado:
print(ejemplo._Ejemplo__atributo_privado)  # Soy un atributo privado y no deberías verme

#----------------------------------------------------------------

class Coche:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.__kilometraje = 0  # Atributo privado

    def conducir(self, kilometros):
        if kilometros >= 0:
            self.__kilometraje += kilometros
        else:
            print(f"\n[!] Los kilómetros deben ser mayores a 0\n")

    def mostrar_kilometros(self):
        return self.__kilometraje


coche = Coche("Toyota", "Corolla")
coche.conducir(150)
print(coche.mostrar_kilometros())

#----------------------------------------------------------------

class Libro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"El libro \"{self.titulo}\" ha sido escrito por {self.autor}"
    
    def __eq__(self, otro):
        return self.autor == otro.autor and self.titulo == otro.titulo

libro = Libro("¿Cómo despertar?", "Albe")
libro_dos = Libro("Señor Ratón", "Camp")
libro_tres = Libro("¿Cómo despertar?", "Albe")
print(libro)  # El libro "¿Cómo despertar?" ha sido escrito por Albe
print(libro_dos)  # El libro "Señor Ratón" ha sido escrito por Camp
print(f"¿Son iguales ambos libros? -> {libro == libro_tres}")  # ¿Son iguales ambos libros? -> True

#----------------------------------------------------------------

class CuentaBancaria:

    def __init__(self, num_cuenta, titular, saldo_inicial=0):
        self.num_cuenta = num_cuenta
        self.titular = titular
        self.__saldo = saldo_inicial  # __saldo como atributo privado

    def depositar_dinero(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"\n[+] Saldo actual en la cuenta: {self.__saldo}")
        else:
            print(f"\n[!] El monto a depositar es incorrecto\n")

    def retirar_dinero(self, cantidad):
        if cantidad > 0 :
            if cantidad > self.__saldo:
                print(f"\n[!] La cantidad a retirar supera el dinero actualmente existente en la cuenta\n")
            else:
                self.__saldo -= cantidad
                print(f"\n[+] Saldo actual en la cuenta: {self.__saldo}")
        else:
            print(f"\n[!] El monto a retirar es incorrecto\n")

    def mostrar_dinero(self):
        return f"\n[+] El saldo actual en al cuenta es: {self.__saldo}"

albe = CuentaBancaria("346578", "Albe Camp")
albe.depositar_dinero(500)
albe.retirar_dinero(350)
print(albe.mostrar_dinero())