#!/usr/bin/env python3

import math_operations

print(math_operations.suma(4, 9))

#----------------------------------------------------------------

# Otra forma de importar, para hacer alusión directa a las clases o funciones definidas
from math_operations import suma, resta, multiplicacion, division
# También se puede usar "*" para importar todo (from math_operations import *)

print(suma(4, 9))
print(resta(4, 9))
print(multiplicacion(4, 9))
print(division(4, 1))

#----------------------------------------------------------------

import math

print(dir(math))  # Para ver casi todos los métodos que da esta librería

print(math.sqrt(26))  # O también sin el math, en caso que importemos desde "math" el "sqrt" (from math import sqrt)