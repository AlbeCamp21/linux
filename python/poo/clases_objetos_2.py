#!/usr/bin/env python3

class Rectangulo:

    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    @property  # Permite acceder al método "area" como si fuera un atributo, sin usar paréntesis (línea 22)
    def area(self):
        return self.ancho * self.alto
    
    def __str__(self):  # Método predefinido que se invoca al llamar solamente al objeto (línea 21)
        return f"\n[+] Propiedades del rectángulo:\n\tAncho:\t{self.ancho}\n\tAlto:\t{self.alto}"

    def __eq__(self, otro):  # Método predefinido que se invoca al comprar dos objetos de una misma clase (línea 23)
        return self.ancho == otro.ancho and self.alto == otro.alto

rect1 = Rectangulo(20, 80)
rect2 = Rectangulo(10, 60)
print(rect1)
print(f"\n[+] El área es {rect1.area}")
print(f"\n[+] ¿Son iguales? -> {rect1 == rect2}")

#----------------------------------------------------------------

class Libro:

    IGV = 0.18

    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    @staticmethod  # No necesitan el objeto para operar
    def es_bestseller(total_ventas):
        return f"\n[+] ¿Es bestseller? -> {total_ventas > 500}"
    
    @classmethod  # Sirve para heredaciones
    def precio_con_igv(cls, precio):
        return precio + precio * cls.IGV
    
class LibroDigital(Libro):

    # Al llamar a "precio_con_igv", usará el "IGV" de LibroDigital, debido a que el método es un classmethod
    IGV = 0.10

mi_libro = Libro("¿Cómo ser un Lammer?", "Albe Camp", 20)
mi_libro_digital = LibroDigital("Ochenta Años", "Felpo", 20)
print(Libro.es_bestseller(7000))
print(f"\n[+] El precio del libro con IGV incluido es de {Libro.precio_con_igv(mi_libro.precio)}")
print(f"\n[+] El precio del libro digital con IGV incluido es de {LibroDigital.precio_con_igv(mi_libro_digital.precio)}")