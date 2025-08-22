#!/usr/bin/env python3

# Renombrando módulos
import math as m

print(m.sqrt(26))

#----------------------------------------------------------------

# Renombrando métodos de un módulo
from math import sqrt as raiz

print(raiz(26))

#----------------------------------------------------------------

import sys

print(sys.path)

# ['/home/albecamp/linux/python/modulos_paquetes/ejemplo_2', '/usr/lib/python313.zip', '/usr/lib/python3.13', '/usr/lib/python3.13/lib-dynload', '/usr/local/lib/python3.13/dist-packages', '/usr/lib/python3/dist-packages']

# Estas son las rutas donde busca python un módulo (parecido a $PATH)
# Primero busca en el directorio actual, y si no encuentra el módulo ahí, va buscando en lo restante de la lista
# Esto se presta para "python library hijacking", que consiste en crear el archivo de un módulo en nuestro directorio actual para suplantar el original
# Por ejemplo
'''
$ import hashlib
$ print(hashlib.__file__)
/usr/lib/python3.13/hashlib.py
'''
# Imaginemos que tenemos un "main.py" que importa "hashlib"
# si en nuestro directorio de trabajo, creamos un archivo "hashlib.py",
# entonces python usará dicho archivo nuevo envés del original
# Ese falso "hashlib.py" podemos modificarlo para aplicar "python library hijacking".