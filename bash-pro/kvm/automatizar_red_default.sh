#!/bin/bash

# Function to show the status of the default network
network_status() {
    virsh net-info default
}

# Function to view the default network configuration
network_config() {
    virsh net-dumpxml default
}

# Function to start or stop the default network
activate_network() {
    read -p "Desea activar (1) o desactivar (0) la red? (1/0): " option
    if [[ "$option" == "1" ]]; then
        virsh net-start default
    elif [[ "$option" == "0" ]]; then
        virsh net-destroy default
    else
        echo "Opcion invalida"
    fi
}

# Function to autostart or disable autostart of the default network
initialize_network() {
    read -p "Desea inicializar (1) o no inicializar (0) la red al iniciar? (1/0): " option
    if [[ "$option" == "1" ]]; then
        virsh net-autostart default
    elif [[ "$option" == "0" ]]; then
        virsh net-autostart --disable default
    else
        echo "Opcion invalida"
    fi
}

# Function to modify the configuration of the default network
modify_network() {
    echo "Modificando la configuracion de la red default..."
    virsh net-edit default
}

# Menu
while true; do
    echo "--- Menu de Configuracion de Red KVM ---"
    echo "----------------------------------------"
    echo "1) Consultar estado de la red"
    echo "2) Ver configuracion de la red"
    echo "3) Activar/Desactivar la red"
    echo "4) Inicializar/No-Inicializar la red"
    echo "5) Modificar configuracion de la red"
    echo "6) Salir"
    read -p "Seleccione una opcion: " choice

    case $choice in
        1) network_status ;;
        2) network_config ;;
        3) activate_network ;;
        4) initialize_network ;;
        5) modify_network ;;
        6) echo "Saliendo..."; break ;;
        *) echo "Opcion invalida. Por favor intente de nuevo." ;;
    esac
done
