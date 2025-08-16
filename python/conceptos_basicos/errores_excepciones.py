#!/usr/bin/env python3

try:
    num = 5/0
except:
    print("No se puede dividir un número entre cero")


try:
    num = 5/0
except ZeroDivisionError:  # Acá se especifica el tipo de error que queremos controlar
    print("No se puede dividir un número entre cero")


try:
    num = "hola"/5
except ZeroDivisionError:
    print("No se puede dividir un número entre cero")
except TypeError:
    print("Las oepracion matemáticas solo se pueden hacer con números")


try:
    num = 7/5
except ZeroDivisionError:
    print("No se puede dividir un número entre cero")
except TypeError:
    print("Las operaciones matemáticas solo se pueden hacer con números")
else:  # En caso que no haya ningun error
    print(f"La división es: {num}")


try:
    num = 7/0
except ZeroDivisionError:
    print("No se puede dividir un número entre cero")
except TypeError:
    print("Las operaciones matemáticas solo se pueden hacer con números")
else:
    print(f"La división es: {num}")
finally:  # Siempre se va a ejecutar esta sección de código, independientemente si hubo una excepción o no
    print("Esto siempre se va a ejecutar")


"""
x = -5
if x < 0:
    raise Exception("No se pueden usar números negativos")  # "raise" siempre para lanzar una excepción
"""

# Más formal y correcto
x = -5
try:
    if x < 0:
        raise Exception("No se pueden usar números negativos")
except Exception as e:
    print(f"Ocurrió un error: {e}")