#!/bin/bash

create_vm() {
    while true; do
        echo "--- Crear Máquina Virtual ---"
        read -p "Nombre de la VM: " vm_name
        read -p "Cantidad de RAM (MB): " ram
        read -p "Cantidad de Disco Duro (GB): " disk
        read -p "Tipo de Sistema Operativo (debian, centos, ubuntu): " os_type
        read -p "Número de CPUs: " cpus
        read -p "Red (puente o NAT): " network

        # Asignar imagen del sistema operativo según el tipo
        case "$os_type" in
            debian)
                iso_path="/var/lib/libvirt/images/debian.iso"
                ;;
            centos)
                iso_path="/var/lib/libvirt/images/centos.iso"
                ;;
            ubuntu)
                iso_path="/var/lib/libvirt/images/ubuntu.iso"
                ;;
            *)
                echo "Tipo de S.O. no válido."
                continue
                ;;
        esac

        # Crear la máquina virtual usando virt-install
        virt-install \
            --name "$vm_name" \
            --ram "$ram" \
            --vcpus "$cpus" \
            --disk size="$disk" \
            --cdrom "$iso_path" \
            --network network=default,model=virtio \
            --graphics vnc,listen=0.0.0.0,port=-1 \
            --os-type linux \
            --noautoconsole

        read -p "¿Desea crear otra máquina virtual? (s/n): " choice
        [[ "$choice" != "s" ]] && break
    done
}

remove_vm() {
    while true; do
        echo "\n--- Eliminar Máquina Virtual ---"
        vms=$(virsh list --all --name)
        echo "Máquinas virtuales disponibles:"
        echo "$vms"

        read -p "Nombre de la VM a eliminar: " vm_name

        if [[ "$vms" =~ (^|[[:space:]])"$vm_name"($|[[:space:]]) ]]; then
            virsh destroy "$vm_name" 2>/dev/null
            virsh undefine "$vm_name"
            echo "Máquina virtual '$vm_name' eliminada."
        else
            echo "Nombre de VM no válido."
        fi

        read -p "¿Desea eliminar otra máquina virtual? (s/n): " choice
        [[ "$choice" != "s" ]] && break
    done
}

while true; do
    echo "--- Menú de Gestión de Máquinas Virtuales KVM ---"
    echo "1) Crear máquina virtual"
    echo "2) Eliminar máquina virtual"
    echo "3) Salir"
    read -p "Seleccione una opción: " option

    case $option in
        1)
            create_vm
            ;;
        2)
            remove_vm
            ;;
        3)
            echo "Saliendo..."
            exit 0
            ;;
        *)
            echo "Opción no válida. Por favor intente nuevamente."
            ;;
    esac
done
