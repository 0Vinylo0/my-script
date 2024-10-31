#!/bin/bash

# Check if KVM is installed
if ! command -v virsh &> /dev/null
then
    echo "KVM is not installed."
    echo "Please specify your operating system (Debian, Ubuntu, CentOS): "
    read os
    case $os in
        Debian|Ubuntu)
            sudo apt update && sudo apt install -y qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils
            ;;
        CentOS)
            sudo yum install -y qemu-kvm libvirt libvirt-python libguestfs-tools virt-install
            ;;
        *)
            echo "Unsupported operating system. Exiting."
            exit 1
            ;;
    esac
fi

# Function to display menu
show_menu() {
    echo "1) Visualizar los pools existentes"
    echo "2) Configurar un pool"
    echo "3) Borrar un pool"
    echo "4) Generar informe de pools"
    echo "5) Salir"
}

# Function to visualize existing pools
view_pools() {
    virsh pool-list --all
}

# Function to configure a pool
configure_pool() {
    echo "a) Crear un nuevo pool"
    echo "b) Mostrar información de los discos duros"
    echo "c) Agregar discos duros a una máquina virtual"
    echo "d) Definir y arrancar un pool"
    read -p "Seleccione una opción: " option

    case $option in
        a)
            read -p "Ingrese el nombre del pool: " pool_name
            read -p "Ingrese la ruta del directorio del pool: " pool_path
            mkdir -p "$pool_path"
            virsh pool-define-as --name "$pool_name" --type dir --target "$pool_path"
            virsh pool-autostart "$pool_name"
            virsh pool-start "$pool_name"
            ;;
        b)
            lsblk
            ;;
        c)
            read -p "Ingrese el nombre de la máquina virtual: " vm_name
            read -p "Ingrese la ruta del disco duro a agregar: " disk_path
            virsh attach-disk "$vm_name" "$disk_path" --target vdb --persistent
            ;;
        d)
            read -p "Ingrese el nombre del pool: " pool_name
            virsh pool-start "$pool_name"
            virsh pool-autostart "$pool_name"
            ;;
        *)
            echo "Opción no válida"
            ;;
    esac
}

# Function to delete a pool
delete_pool() {
    view_pools
    read -p "Ingrese el nombre del pool que desea borrar: " pool_name
    virsh pool-destroy "$pool_name"
    virsh pool-undefine "$pool_name"
}

# Function to generate a report
generate_report() {
    report_file="Informe_Pool.txt"
    echo "Generando informe..."
    echo "Pools creados:" > "$report_file"
    virsh pool-list --all >> "$report_file"
    echo -e "\nPools activos:" >> "$report_file"
    virsh pool-list >> "$report_file"
    echo -e "\nPools con arranque automático:" >> "$report_file"
    virsh pool-autostart >> "$report_file"
    echo "Informe generado en $report_file"
}

# Main loop
while true; do
    show_menu
    read -p "Seleccione una opción: " choice
    case $choice in
        1)
            view_pools
            ;;
        2)
            configure_pool
            ;;
        3)
            delete_pool
            ;;
        4)
            generate_report
            ;;
        5)
            echo "Saliendo..."
            exit 0
            ;;
        *)
            echo "Opción no válida, intente nuevamente."
            ;;
    esac
done