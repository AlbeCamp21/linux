#!/usr/bin/env python3

class Caja:

    def __init__(self, *items):
        self.items = items

    def mostrar_items(self):
        for item in self.items:
            print(item)
        print(type(self.items))

    def __len__(self):  # Método especial para definir "len(objeto)"
        return len(self.items)
        
caja = Caja("Manzana", "Plátano", "Kiwi", "Pera")
caja.mostrar_items()  # Imprime las frutas y <class 'tuple'>
print(len(caja))  # 4

#----------------------------------------------------------------

class Pizza:

    def __init__(self, size, *ingredientes):
        self.size = size
        self.ingredientes = ingredientes

    def descripcion(self):
        print(f"Esta pizza tiene {self.size} cm de longitud y los ingrediente son: {', '.join(self.ingredientes)}")
        
        
pizza = Pizza(12, "Chorizo", "Jamón", "Bacon", "Queso", "Cebolla")
pizza.descripcion()  # Esta pizza tiene 12 cm de longitud y los ingrediente son: Chorizo, Jamón, Bacon, Queso, Cebolla

#----------------------------------------------------------------

class MiLista:

    def __init__(self):
        self.data = [1, 2, 3, 4, 5]

    # En caso que tengamos varias listas en una clase, este metodo sirve decirle a python a que lista nos referimos al poner "objeto[index]"
    def __getitem__(self, index):
        return self.data[index]

lista = MiLista()
print(lista[2])  # También se podría poner "lista.data[2]", pero así es más práctico gracias al método especial

#----------------------------------------------------------------

class Saludo:

    def __init__(self, saludo):
        self.saludo = saludo

    # Método especial pasa usar "objeto(argumento)"
    def __call__(self, nombre):
        return f"{self.saludo} {nombre}!"

hola = Saludo("¡Hola")
print(hola("Albe"))  # ¡Hola Luis!

#----------------------------------------------------------------

class Punto:

    def __init__(self, x ,y):
        self.x = x
        self.y = y

    # Método especial para indicar a Python como se debe realizar una suma, también hay métodos especiales para otras operaciones
    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Punto(2, 8)
p2 = Punto(4, 9)
print(p1 + p2)  # (6, 17)
print(p1)  # (2, 8)

#----------------------------------------------------------------

class Contador:

    def __init__(self, limite):
        self.limite = limite

    def __iter__(self):
        self.contador = 0
        return self
    
    def __next__(self):
        if self.contador < self.limite:
            self.contador += 1
            return self.contador
        else:
            raise StopIteration
        
c = Contador(5)
for i in c:
    print(i)