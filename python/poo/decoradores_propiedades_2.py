#!/usr/bin/env python3

# *args

def suma(*args):
    print(type(args))  # <class 'tuple'>
    print(args)  # (2, 3, 4, 5, 7, 1, 14, 4, 54)
    return sum(args)

print(suma(2, 3, 4, 5, 7, 1, 14, 4, 54))

# **kwargs

def presentacion(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    print(kwargs)  # {'nombre': 'Albe', 'edad': 74, 'ciudad': 'New York', 'profesion': 'Estudiante'}
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

presentacion(nombre="Albe", edad=74, ciudad="New York", profesion="Estudiante")

#----------------------------------------------------------------

class Circunferencia:

    def __init__(self, radio):
        self._radio = radio

    @property  # Getter
    def radio(self):
        return self._radio
    
    @property  # Getter
    def diametro(self):
        return 2 * self._radio
    
    @property  # Getter
    def area(self):
        return 3.1415 * (self._radio ** 2)
    
    @radio.setter  # Setter
    def radio(self, valor):
        self._radio = valor

c = Circunferencia(5)
print(c.radio)  # 5
print(c.diametro)  # 10
print(round(c.area, 3))  # 78.538

c.radio = 10
print(c.radio)  # 10
print(c.diametro)  # 20
print(round(c.area, 3))  # 314.15