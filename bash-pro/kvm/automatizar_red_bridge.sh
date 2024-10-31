#!/bin/bash

ver_configuracion_red() {
    echo "Configuración actual de la red:"
    brctl show
    ip addr show
}

definir_red_bridge_estatica() {
    read -p "Introduce el nombre del bridge (ejemplo: br0): " bridge_name
    read -p "Introduce el nombre de la interfaz asociada (ejemplo: ensXX): " interfaz

    echo "Creando el bridge $bridge_name..."
    sudo brctl addbr $bridge_name
    sudo brctl addif $bridge_name $interfaz
    sudo ip link set dev $bridge_name up
    
    echo "Bridge $bridge_name configurado con la interfaz $interfaz"
}

verificar_bridge_existente() {
    read -p "Introduce el nombre del bridge a verificar (ejemplo: br0): " bridge_name
    if brctl show | grep -q "$bridge_name"; then
        echo "El bridge $bridge_name existe."
        if ip link show | grep -q "$bridge_name"; then
            echo "El bridge $bridge_name está asociado a una interfaz."
        else
            echo "El bridge $bridge_name no está asociado a una interfaz."
        fi
    else
        echo "El bridge $bridge_name no existe."
    fi
}

activar_noactivar_red() {
    read -p "Introduce el nombre del bridge (ejemplo: br0): " bridge_name
    read -p "Deseas activar (up) o desactivar (down) el bridge? (up/down): " accion
    if [ "$accion" == "up" ]; then
        sudo ip link set dev $bridge_name up
        echo "El bridge $bridge_name ha sido activado."
    elif [ "$accion" == "down" ]; then
        sudo ip link set dev $bridge_name down
        echo "El bridge $bridge_name ha sido desactivado."
    else
        echo "Acción no reconocida."
    fi
}

modificar_configuracion() {
    echo "Modificando la configuración del bridge..."
    read -p "Introduce el nombre del bridge (ejemplo: br0): " bridge_name
    read -p "Introduce la nueva interfaz a asociar (ejemplo: ensXX): " nueva_interfaz
    
    echo "Eliminando interfaces actuales del bridge $bridge_name..."
    sudo brctl delif $bridge_name "$(brctl show $bridge_name | awk 'NR==2 {print $4}')"
    
    echo "Asociando el bridge $bridge_name a la nueva interfaz $nueva_interfaz..."
    sudo brctl addif $bridge_name $nueva_interfaz
    echo "Configuración del bridge $bridge_name modificada."
}

while true; do
    echo "--- Menú de configuración de red en KVM ---"
    echo "-------------------------------------------"
    echo "1) Ver la configuración de la red"
    echo "2) Definir una red bridge estática"
    echo "3) Verificar la existencia de un bridge y su interfaz asociada"
    echo "4) Activar/Desactivar la red"
    echo "5) Modificar la configuración del bridge"
    echo "6) Salir"
    read -p "Selecciona una opción (1-6): " opcion

    case $opcion in
        1)
            ver_configuracion_red
            ;;
        2)
            definir_red_bridge_estatica
            ;;
        3)
            verificar_bridge_existente
            ;;
        4)
            activar_noactivar_red
            ;;
        5)
            modificar_configuracion
            ;;
        6)
            echo "Saliendo del script."
            exit 0
            ;;
        *)
            echo "Opción no válida, por favor selecciona una opción entre 1 y 6."
            ;;
    esac
done
