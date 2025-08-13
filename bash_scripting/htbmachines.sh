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
    echo -e "\t${moradoColor}i)${finColor} ${grisColor}Buscar por dirección IP${finColor}"
    echo -e "\t${moradoColor}d)${finColor} ${grisColor}Buscar por la dificultad de las máquinas${finColor}"
    echo -e "\t${moradoColor}o)${finColor} ${grisColor}Buscar por el sistema operativo de las máquinas${finColor}"
    echo -e "\t${moradoColor}y)${finColor} ${grisColor}Obtener link de la resolución de la máquina en Youtube${finColor}"
    echo -e "\t${moradoColor}h)${finColor} ${grisColor}Mostrar panel de ayuda${finColor}"
}

function searchMachine(){
    machineName="$1"
    commandValidator="$(cat bundle.js | grep "name: \"$machineName\"")"
    if [ -z "$commandValidator" ]; then
        echo -e "\n${rojoColor}[!]${finColor} ${grisColor}La máquina${finColor} ${moradoColor}$machineName${finColor} ${grisColor}no existe, intente con otra${finColor}"
    else
        echo -e "\n${verdeColor}[+]${finColor} ${grisColor}Listando las propiedades de la máquina${finColor} ${moradoColor}$machineName${finColor}${grisColor}:${finColor}\n"
        cat bundle.js | awk "/name: \"$machineName\"/,/resuelta:/" | grep -vE "id:|sku|resuelta" | tr -d '"' | tr -d "," | sed 's/^ *//'
    fi    
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

function searchIP(){
    ipAddress="$1"
    commandValidator="$(cat bundle.js | grep "ip: \"$ipAddress\"")"
    machineName="$(cat bundle.js | grep "ip: \"$ipAddress\"" -B 3 | grep "name: " | awk 'NF{print $NF}' | tr -d '"' | tr -d ',')"
    if [ -z "$commandValidator" ]; then
        echo -e "\n${rojoColor}[!]${finColor} ${grisColor}La IP${finColor} ${moradoColor}$ipAddress${finColor} ${grisColor}no existe, intente con otra${finColor}"
    else
        echo -e "\n${verdeColor}[+]${finColor} ${grisColor}La máquina correspondiente para la IP${finColor} ${azulColor}$ipAddress${finColor} ${grisColor}es${finColor} ${moradoColor}$machineName${finColor}"
    fi
}

function getYoutubeLink(){
    machineName="$1"
    commandValidator="$(cat bundle.js | grep "name: \"$machineName\"")"
    if [ -z "$commandValidator" ]; then
        echo -e "\n${rojoColor}[!]${finColor} ${grisColor}La máquina${finColor} ${moradoColor}$machineName${finColor} ${grisColor}no existe, intente con otra${finColor}"
    else
        youtubeLink="$(cat bundle.js | awk "/name: \"$machineName\"/,/resuelta:/" | grep -vE "id:|sku:|resuelta" | tr -d '"' | tr -d "," | sed 's/^ *//' | grep youtube | awk 'NF{print $NF}')"
        echo -e "\n${verdeColor}[+]${finColor} ${grisColor}El tutorial de la máquina${grisColor} ${moradoColor}$machineName${finColor} ${grisColor}está en el siguiente enlace:${finColor} ${azulColor}$youtubeLink${finColor}"
    fi
}

function getMachinesDifficulty(){
    difficulty="$1"
    commandValidator="$(cat bundle.js | grep "dificultad: \"$difficulty\"")"
    results_check="$(cat bundle.js | grep "dificultad: \"$difficulty\"" -B 5 | grep "name:" | awk 'NF {print $NF}' | tr -d '"' | tr -d "," | column)"
    if [ -z "$commandValidator" ]; then
        echo -e "\n${rojoColor}[!]${finColor} ${grisColor}La dificultad${finColor} ${moradoColor}$difficulty${finColor} ${grisColor}no existe, opciones válidas:\n\n\t- Fácil\n\t- Media\n\t- Difícil\n\t- Insane${finColor}"
    else
        echo -e "\n${verdeColor}[+]${finColor} ${grisColor}Listando máquinas de dificultad${finColor} ${moradoColor}$difficulty${finColor}${grisColor}:${finColor}\n"
        cat bundle.js | grep "dificultad: \"$difficulty\"" -B 5 | grep "name:" | awk 'NF {print $NF}' | tr -d '"' | tr -d "," | column
    fi
}

function getOSMachines(){
    os="$1"
    commandValidator="$(cat bundle.js | grep "so: \"$os\"")"
    if [ -z "$commandValidator" ]; then
        echo -e "\n${rojoColor}[!]${finColor} ${grisColor}El sistema operativo${finColor} ${moradoColor}$os${finColor} ${grisColor}no existe, intente con otra${finColor}"
    else
        echo -e "\n${verdeColor}[+]${finColor} ${grisColor}Mostrando máquinas con sistema operativo${finColor} ${moradoColor}$os${finColor}\n"
        cat bundle.js | grep "so: \"$os\"" -B 5 | grep "name: " | awk 'NF {print $NF}' | tr -d '"' | tr -d "," | column
    fi
}

function getOSDifficultyMachines(){
    difficulty="$1"
    os="$2"
    commandValidator_difficulty="$(cat bundle.js | grep "dificultad: \"$difficulty\"")"
    commandValidator_os="$(cat bundle.js | grep "so: \"$os\"")"
    if [ -z "$commandValidator_difficulty" ] || [ -z "$commandValidator_os" ]; then
        echo -e "\n${rojoColor}[!]${finColor} ${grisColor}Alguno de los parámetros no es válido, intente nuevamente${finColor}"
    else
        echo -e "\n${verdeColor}[+]${finColor} ${grisColor}Listando máquinas por dificultad${finColor} ${moradoColor}$difficulty${finColor} ${grisColor}y sistema operativo${finColor} ${moradoColor}$os${finColor}\n"
        cat bundle.js | grep "so: \"$os\"" -C 4 | grep "dificultad: \"$difficulty\"" -B 5 | grep "name: " | awk 'NF {print $NF}' | tr -d '"' | tr -d "," | column
    fi
}

# Indicadores
declare -i parameter_counter=0  # "-i" para integer

# Chivatos
declare -i chivato_difficulty=0
declare -i chivato_os=0

while getopts "m:ui:y:hd:o:" arg; do  # Los que necesitan argumentos se les pone con ":"
    case $arg in 
        m) machineName="$OPTARG"; let parameter_counter+=1;;  # "$OPTARG" para agarrar el argumento del parámetro
        u) let parameter_counter+=2;;
        i) ipAddress="$OPTARG"; let parameter_counter+=3;;
        y) machineName="$OPTARG"; let parameter_counter+=4;;
        d) difficulty="$OPTARG"; chivato_difficulty=1; let parameter_counter+=5;;
        o) os="$OPTARG"; chivato_os=1; let parameter_counter+=6;;
        h) ;;  # siempre se acaba en ";;"
    esac
done

if [ $parameter_counter -eq 1 ]; then
    searchMachine $machineName
elif [ $parameter_counter -eq 2 ]; then
    updateFiles
elif [ $parameter_counter -eq 3 ]; then
    searchIP $ipAddress
elif [ $parameter_counter -eq 4 ]; then
    getYoutubeLink $machineName
elif [ $parameter_counter -eq 5 ]; then
    getMachinesDifficulty $difficulty
elif [ $parameter_counter -eq 6 ]; then
    getOSMachines $os
elif [ $chivato_difficulty -eq 1 ] && [ $chivato_os -eq 1 ]; then
    getOSDifficultyMachines $difficulty $os
else
    helpPanel
fi