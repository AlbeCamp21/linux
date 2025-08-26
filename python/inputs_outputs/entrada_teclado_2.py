#!/usr/bin/env python3

from getpass import getpass

password = getpass("\n[+] Introduce tu contraseña: ")  # getpass hace que no se vea lo que introducimos (inputs)
print(f"\n[+] Tu contraseña es: {password}") # Podemos ver el contenido simplemente imprimiéndolo