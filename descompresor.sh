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
    echo -e "\n\n${rojoColor}[!] Saliendo...${finColor}\n"
    exit 0
}

# Ctrl + C
trap ctrl_c INT

# Solicitando el comprimido inicial
echo -e "${azulColor}[?] Introduce el nombre del archivo comprimido:${finColor} "
read -r first_file_name

# Verificando que el archivo existe
if [ ! -f "$first_file_name" ]; then
    echo -e "\n${rojoColor}[!] Error: El archivo '$first_file_name' no existe.${finColor}"
    exit 1
fi

decompressed_file_name="$(7z l "$first_file_name" | tail -n 3 | head -n 1 | awk 'NF{print $NF}')"
7z x "$first_file_name" &>/dev/null

while [ $decompressed_file_name ]; do
    echo -e "\n${turquesaColor}[+] Nuevo archivo descomprimido:${finColor} $decompressed_file_name"
    7z x "$decompressed_file_name" &>/dev/null
    decompressed_file_name="$(7z l "$decompressed_file_name" 2>/dev/null | tail -n 3 | head -n 1 | awk 'NF{print $NF}')"
done

echo -e "\n${verdeColor}[+] Descompresión completada.${finColor}"
