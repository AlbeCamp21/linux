#!/usr/bin/env python3

class Persona():

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Estudiante(Persona):

    def __init__(self, nombre, edad, id):
        super().__init__(nombre, edad)
        self.id = id
        self.cursos = {}

    def __repr__(self):
        return f"\n[+] Alumno {self.id}:\n\t- Nombre: {self.nombre}\n\t- Edad: {self.edad}\n\t- Cursos: {self.cursos.keys()}"
    
class Curso():

    def __init__(self, nombre, codigo, profesor):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
        self.estudiantes = {}

    def agregar_estudiante(self, estudiante, academia):
        if estudiante.id in academia.estudiantes_academia:  # Verificar si el estudiante está matriculado en la academia
            if estudiante.id not in self.estudiantes:  # Verificar si el estudiante aún no está en el curso
                self.estudiantes[estudiante.id] = estudiante
                estudiante.cursos[self.codigo] = self
                return f"\n[+] Se agregó correctamente al estudiante '{estudiante.id}' al curso '{self.codigo}'."
            else:
                return f"\n[!] No se pudo agregar al estudiante '{estudiante.id}' al curso '{self.codigo}'."
        else:
            return f"\n[!] El estudiante con id '{estudiante.id}' no existe."
    
    @property
    def mostrar_estudiantes(self):
        return [estudiante for estudiante in self.estudiantes.values()]  # Corregir ya que imprime una lista?
    # ----------------------------------------------------------------------------
    
    def __repr__(self):
        return f"\n[+] Curso {self.codigo}:\n\t- Nombre: {self.nombre}\n\t- Profesor: {self.profesor}"
    
class Academia():

    def __init__(self):
        self.cursos_academia = {}
        self.estudiantes_academia = {}

    def agregar_curso_a_academia(self, curso):
        if curso.codigo not in self.cursos_academia:
            self.cursos_academia[curso.codigo] = curso
            return f"\n[+] Curso {curso.codigo} creado correctamente."
        else:
            return f"\n[!] No se pudo crear el curso con código {curso.codigo}."

    def agregar_estudiante_a_academia(self, estudiante):
        if estudiante.id not in self.estudiantes_academia:  # Verificar si aún no está matriculado el estudiante
            self.estudiantes_academia[estudiante.id] = estudiante
            return f"\n[+] Estudiante {estudiante.id} matriculado correctamente en la academia."
        else:  # Si el estudiante ya está matriculado
            return f"\n[!] No se pudo matricular al alumno con código {estudiante.id}."
        

academia = Academia()

estudiante1 = Estudiante("Luis Alanya", 23, "20210290J")
estudiante2 = Estudiante("María Torres", 21, "20200315K")
estudiante3 = Estudiante("Juan Pérez", 22, "20230408L")
estudiante4 = Estudiante("Ana Castillo", 20, "20220522M")
estudiante5 = Estudiante("Carlos Ramírez", 24, "20210611N")
estudiante6 = Estudiante("Sofía Guzmán", 23, "20200703P")

curso1 = Curso("Aritmética", "CC-421", "Leo Ruiz")
curso2 = Curso("Geometría", "IF-123", "Gustavo Petro")

print(academia.agregar_estudiante_a_academia(estudiante1))
print(academia.agregar_estudiante_a_academia(estudiante2))
print(academia.agregar_estudiante_a_academia(estudiante3))
print(academia.agregar_estudiante_a_academia(estudiante1))  # Estudiante ya registrado

print(academia.agregar_curso_a_academia(curso1))

print(estudiante1)
print(curso1)
print(curso1.agregar_estudiante(estudiante1,academia))  # Usuario matriculado
print(curso1.agregar_estudiante(estudiante6,academia))  # Usuario no matriculado
print(curso1.mostrar_estudiantes)