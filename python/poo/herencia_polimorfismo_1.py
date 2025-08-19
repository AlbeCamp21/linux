#!/usr/bin/env python3

# =============== HERENCIA ===============

class Animal:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        raise NotImplementedError("Las subclases definidas deben implementar este método")
        # "pass" también se puede poner simplemente

class Gato(Animal):  # Gato(Animal(gato, nombre))

    def hablar(self):
        return f"{self.nombre} dice ¡Miau!"
    
class Perro(Animal):

    def hablar(self):
        return f"{self.nombre} dice ¡Guau!"
 
gato = Gato("Michi")
perro = Perro("Newton")
print(gato.hablar())
print(perro.hablar())


# =============== POLIMORFISMO ===============

class Animal:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        raise NotImplementedError("Las subclases definidas deben implementar este método")
        # "pass" también se puede poner simplemente, o también un return cualquiera

class Gato(Animal):  # Gato(Animal(gato, nombre))

    def hablar(self):
        return f"¡Miau!"
    
class Perro(Animal):

    def hablar(self):
        return f"¡Guau!"

def hacer_hablar(objeto):  # La clase del objeto que se use usará su propio método
    print(f"{objeto.nombre} dice {objeto.hablar()}")


gato = Gato("Michi")
perro = Perro("Newton")
hacer_hablar(gato)
hacer_hablar(perro)