#!/usr/bin/env python3

nombre = input("\n[+] Dime tu nombre: ")

print(f"\n[+] Perfecto, ahora sé que te llamas {nombre}")

#----------------------------------------------------------------

edad = int(input("\n[+] Dime tu edad: "))

print(f"\n[+] Perfecto, el año que viene deberías cumplir {edad + 1} años")

#----------------------------------------------------------------

while True:
    try:
        edad = int(input("\n[+] Dime tu edad: "))
        print(f"\n[+] Perfecto, el año que viene deberías cumplir {edad + 1} años")
        break
    except ValueError:
        print(f"\n[!] El tipo de dato introducido es incorrecto")
