#!/usr/bin/env python3

with open("/etc/hosts", "r") as f:
    file_content = f.read()

print(file_content)  # Muestra contenido de "/etc/hosts"

#----------------------------------------------------------------
# Este objeto ("f") es iterable

with open("/etc/hosts", "r") as f:
    for line in f:
        print(line.strip())  # "strip()" para que imprima sin saltos de líneas que son generados al realizar por esta forma

#----------------------------------------------------------------
# Introducir múltiples líneas que están en un iterable

mi_lista = ["Primera línea\n", "Segunda línea\n", "Tercera línea\n", "Cuarta línea"]

with open("example_2.txt", "w") as f:
    f.writelines(mi_lista)
'''
Primera línea
Segunda línea
Tercera línea
Cuarta línea
'''