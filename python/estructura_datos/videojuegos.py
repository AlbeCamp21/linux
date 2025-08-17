#!/usr/bin/env python3

juegos = ["Super Mario Bros", "Zelda: Breath of the Wild", "Dota 2", "League of Legends", "Balatro", "Cyberpunk 2077", "Final Fantasy VII"]
tope = 500

# Géneros
generos = {
    "Super Mario Bros": "Aventura",
    "Zelda: Breath of the Wild": "Aventura",
    "Dota 2": "MOBA",
    "League of Legends": "MOBA",
    "Balatro": "Roguelike",
    "Cyberpunk 2077": "Rol",
    "Final Fantasy VII": "Rol"
}

# Ventas y Stock
ventas_y_stock = {
    "Super Mario Bros": (400, 200),
    "Zelda: Breath of the Wild": (600, 20),
    "Dota 2": (150, 200),
    "League of Legends": (1500, 120),
    "Balatro": (2000, 10),
    "Cyberpunk 2077": (60, 120),
    "Final Fantasy VII": (924, 3)
}

# Clientes
clientes = {
    "Super Mario Bros": {"Pepe", "Zoey", "Emiliano", "Gustavo"},
    "Zelda: Breath of the Wild": {"Zoey", "Juan", "Romyna", "Albe", "Emiliano"},
    "Dota 2": {"Albe", "Sebastián"},
    "League of Legends": {"Juan", "Camola", "Belén", "Gustavo", "Pepe", "Rodrigo"},
    "Balatro": {"Albe", "Kenny", "Lema"},
    "Cyberpunk 2077": {"Lema", "Gustavo"},
    "Final Fantasy VII": {"Gustavo", "Zoey", "Pepe", "Rodrigo"}
}

# Sumario
def sumario(juego):
    print(f"\n[i] Resumen del juego: {juego}\n")
    print(f"\t[+] Género del juego: {generos[juego]}")
    print(f"\t[+] Total de ventas para este juego: {ventas_y_stock[juego][0]} unidades")
    print(f"\t[+] Total de stock para este juego: {ventas_y_stock[juego][1]} unidades")
    print(f"\t[+] Algunos clientes que han adquirido el juego: {', '.join(clientes[juego])}")  # Separa elementos con el objeto entre comillas



ventas_totales = lambda: sum(ventas for juego, (ventas, _) in ventas_y_stock.items() if ventas_y_stock[juego][0] > tope)

print(f"\n\t\t====== Ver productos con ventas mayores a cierto tope =======")
tope = int(input(f"\n[!] Introduce el tope de ventas: "))
print(f"\n\t\t====== Mostrando productos con ventas mayores a {tope} =======")
for juego in juegos:
    if ventas_y_stock[juego][0] > tope:
        sumario(juego)
print(f"\n[+] El total de ventas de todos los productos con venta mayores a {tope} ha sido de {ventas_totales()} productos")