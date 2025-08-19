#!/usr/bin/env python3

class Dispositivos:

    def __init__(self, modelo):
        self.modelo = modelo

    def escanear_vulnerabilidades(self):
        raise NotImplementedError("Este método debe de ser definido para el resto de subclases existentes")
    
class Ordenador(Dispositivos):

    def escanear_vulnerabilidades(self):
        return f"[+] Análisis de vulnerabilidades concluido: Actualización de software necesario, múltiples desactualizaciones de software detectado"
    
class Router(Dispositivos):

    def escanear_vulnerabilidades(self):
        return f"[+] Análisis de vulnerabilidades concluido: Múltiples puertos críticos detectados como abiertos, es recomendable cerrar estos puertos"
    
class TelefonoMovil(Dispositivos):

    def escanear_vulnerabilidades(self):
        return f"[+] Análisis de vulnerabilidades concluido: Múltiples aplicaciones detectadas con permisos excesivos"
    
def realizar_escaneo(dispositivo):

    print(dispositivo.escanear_vulnerabilidades())

pc = Ordenador("Dell XPS")
router = Router("Tp-Link Archer C50")
movil = TelefonoMovil("Samsung Galaxy S21")
realizar_escaneo(pc)
realizar_escaneo(router)
realizar_escaneo(movil)

#----------------------------------------------------------------

class A:

    def __init__(self, x):
        self.x = x
        print(f"Valor en x: {self.x}")

class B(A):

    def __init__(self, x, y):
        self.y = y
        super().__init__(x)  # Llama al constructor de clase "A"
        print(f"Valor en y: {self.y}")

b = B(2, 10)
# Valor en x: 2
# Valor en y: 10

#----------------------------------------------------------------

class A:

    def saludo(self):
        return f"Saludo desde A"
    
class B(A):

    def saludo(self):
        original = super().saludo()  # Llama al método "saludo" de la clase "A"
        print(f"{original}, pero también saludo desde B")

saludo = B()
saludo.saludo()  # Saludo desde A, pero también saludo desde B

#----------------------------------------------------------------

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludo(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años"

class Empleado(Persona):

    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)  # Llama al constructor de "Persona", definiendo los atributos "nombre" y "edad"
        self.salario = salario

    def saludo(self):

        return f"{super().saludo()}, y cobro {self.salario}  dólares anuales"  # Llama al método "saludo" de "Persona"

persona = Persona("Albe", 31)
print(persona.saludo())  # Hola, soy Albe y tengo 31 años
persona_dos = Empleado("Camp", 54, 1200)
print(persona_dos.saludo())  # Hola, soy Camp y tengo 54 años, y cobro 1200  dólares anuales