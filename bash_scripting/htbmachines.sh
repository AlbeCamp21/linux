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
    tput cnorm && exit 1
}

# Ctrl+C
trap ctrl_c INT

# Variables globales
main_url="https://htbmachines.github.io/bundle.js"

function helpPanel(){
    echo -e "\n${amarilloColor}[+]${finColor} ${grisColor}Uso:${grisColor}"
    echo -e "\t${moradoColor}u)${finColor} ${grisColor}Descargar o actualizar archivos necesarios${finColor}"
    echo -e "\t${moradoColor}m)${finColor} ${grisColor}Buscar por un nombre de máquina${finColor}"
    echo -e "\t${moradoColor}h)${finColor} ${grisColor}Mostrar panel de ayuda${finColor}"
}

function searchMachine(){
    machineName="$1"
    echo $machineName
    # También podría haber sido simplement: echo $1
}

function updateFiles(){
    tput civis  # Ocultar cursor
    if [ ! -f bundle.js ]; then  # Comprobando si no existe el archivo
        echo -e "\n${amarilloColor}[+]${finColor} ${grisColor}Descargando archivos necesarios...${finColor}"
        curl -s $main_url > bundle.js
        js-beautify bundle.js 2>/dev/null | sponge bundle.js
        echo -e "\n${verdeColor}[+]${finColor} ${grisColor}Todos los archivos han sido descargados${finColor}"
    else  # Comprobando si hay actualizaciones
        echo -e "\n${amarilloColor}[+]${finColor} ${grisColor}Comprobando si hay actulizaciones pendientes...${finColor}"
        curl -s $main_url > bundle_temp.js
        js-beautify bundle_temp.js 2>/dev/null | sponge bundle_temp.js
        md5_temp_value=$(md5sum bundle_temp.js | awk '{print $1}')  # Hash del nuevo archivo
        md5_original_value=$(md5sum bundle.js | awk '{print $1}')  # Hash del actual archivo
        if [ "$md5_temp_value" == "$md5_original_value" ]; then
            echo -e "${verdeColor}\n[+]${finColor} ${grisColor}No se han detectado actualizaciones${finColor}"
            rm bundle_temp.js
        else
            echo -e "${amarilloColor}\n[+]${finColor} ${grisColor}Se han encontrado actualizaciones disponibles${finColor}"
            sleep 1
            rm bundle.js && mv bundle_temp.js bundle.js
            echo -e "\n${verdeColor}[+]${finColor} ${grisColor}Los archivos han sido actualizados${finColor}"
        fi
    fi
    tput cnorm  # Mostrar cursor
}

# Indicadores
declare -i parameter_counter=0  # "-i" para integer

while getopts "m:uh" arg; do  # Los que necesitan argumentos se les pone con ":"
    case $arg in 
        m) machineName=$OPTARG; let parameter_counter+=1;;  # "$OPTARG" para agarrar el argumento del parámetro
        u) let parameter_counter+=2;;
        h) helpPanel;;  # siempre se acaba en ";;"
    esac
done

if [ $parameter_counter -eq 1 ]; then
    searchMachine $machineName
elif [ $parameter_counter -eq 2 ]; then
    updateFiles
else
    helpPanel
fi