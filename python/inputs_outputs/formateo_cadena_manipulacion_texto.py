#!/usr/bin/env python3

cadena = "   \n   Hola mundo!! \t "
# "strip()" quita espacios, tabulaciones y saltos de línea al inicio y al final de una cadena
print(cadena.strip())  # Hola mundo!!

#----------------------------------------------------------------

cadena = "Hola mundo"
print(cadena.lower())  # hola mundo
print(cadena.upper())  # HOLA MUNDO
print(cadena.replace("o", "x"))  # Hxla mundx
cadena = "hola mundo"
print(cadena.capitalize())  # Hola mundo
print(cadena.title())  # Hola Mundo
cadena = "hoLa MuNdo"
print(cadena.swapcase())  # HOlA mUnDO

#----------------------------------------------------------------

# "replace()" también puede servir para quitar elementos de una cadena
cadena = "Soy Albe, y ,no me gusta, la, coma,"
print(cadena.replace(",",""))  # Soy Albe y no me gusta la coma

#----------------------------------------------------------------

cadena = "¡Hola mundo!"
nueva_cadena = cadena.split()  # "split()" separa la cadena por espacio (default) y lo convierte en una lista
print(nueva_cadena)  # ['¡Hola', 'mundo!']
cadena = "¡Hola:mundo soy Albe,Camp!"
nueva_cadena = cadena.split(":")
print(nueva_cadena)  # ['¡Hola', 'mundo soy Albe,Camp!']

#----------------------------------------------------------------

s = "Hola mundo"
# Comprabando si una cadena inicia con una determinada palabra, letra, etc.
print(s.startswith("Hola"))  # True
print(s.startswith("H"))  # True
print(s.startswith("h"))  # False
# Comprabando si una cadena termina con una determinada palabra, letra, etc.
print(s.endswith("ndo"))  # True
print(s.endswith("O"))  # False
print(s.endswith("o"))  # True

#----------------------------------------------------------------

s = "Hola mundo"
# "find()" nos devuelve el índice de la cadena que pasemos por parámetro, en caso que no haya, devuelve -1
# "index()", metodo parecido, pero cuando no hay la cadena que le pasamos, devuelve un ValueError
print(s.find("hola"))  # -1
print(s.find("ola"))  # 1
print(s.find("mun"))  # 5
print(s.find("H"))  # 0

#----------------------------------------------------------------

s = "Esto es una prueba para contar el total de caracteres que hay en esta frase"
# "count()" devuelve la cantidad de veces que aparece un caracter o cadena en una cadena, diferencia mayúsculas de minúsculas
print(f"\n[+] Total de veces que sale el caracter 'e': {s.count("e")}")  # 10
print(f"\n[+] Total de veces que sale la cadena 'to': {s.count("to")}")  # 2

#----------------------------------------------------------------

# "join()" para mostrar los elementos de una lista separados por un delimitador que podemos definir
cadena = ["Hola", "Mundo"]
print(" ".join(cadena))  # Hola Mundo
nombres = ["Albe", "Felpo", "Zoey"]
print(", ".join(nombres))  # Albe, Felpo, Zoey
print(f"\n[+] Los nombres son: {' y '.join(nombres)}")  # [+] Los nombres son: Albe y Felpo y Zoey

#----------------------------------------------------------------

s = "abc"
# "isalpha()" para verificar si una cadena contiene solamente letras del abecedario
print(s.isalpha())  # True
s = "abc123"
print(s.isalpha())  # False
# "isdigit()" para verificar si una cadena contiene solamente números
s = "123"
print(s.isdigit())  # True
# Hay varios verificadores parecidos como: istitle, islower, isupper, isspace

#----------------------------------------------------------------

# Reemplazo Avanzado

cadena = "Hola, soy Albe, y no me gusta el invierno"
tabla = str.maketrans("aei", "lmn")  # Define los reemplazos: 'l' por 'a', 'e' por 'm' e 'i' por 'n'
nueva_cadena = cadena.translate(tabla)  # Aplicando los reemplazos a una nueva variable
print(nueva_cadena)  # Holl, soy Albm, y no mm gustl ml nnvnmrno