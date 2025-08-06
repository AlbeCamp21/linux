#!/bin/bash

verdeColor="\e[0;32m\033[1m"
finColor="\033[0m\e[0m"
rojoColor="\e[0;31m\033[1m"
azulColor="\e[0;34m\033[1m"
amarilloColor="\e[0;33m\033[1m"
moradoColor="\e[0;35m\033[1m"
turquesaColor="\e[0;36m\033[1m"
grisColor="\e[0;37m\033[1m"

function ctrl_c(){
    echo -e "\n\n${amarilloColor}[!] Saliendo...${finColor}\n"
    tput cnorm; exit 1
}

# Ctrl+C
trap ctrl_c INT

# Ocultar el cursor durante la ejecución
tput civis

echo -e "\n${moradoColor}====== SCANER DE PUERTOS ======${finColor}\n"
for port in $(seq 1 65535); do
    (echo '' > /dev/tcp/127.0.0.1/$port) 2>/dev/null && echo -e "${verdeColor}[+] $port - OPEN${finColor}" &
done; wait
echo -e "\n${moradoColor}[!] Scaneo completo.${finColor}\n"

# Recuperando el cursor
tput cnorm