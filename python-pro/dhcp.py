from scapy.all import *

def enviar_paquete_dhcp_discover(ip_cliente):
    # Generar una dirección MAC aleatoria
    mac_cliente = RandMAC()
    
    # Crear el paquete Ethernet
    eth = Ether(dst="ff:ff:ff:ff:ff:ff", src=mac_cliente, type=0x0800)
    
    # Crear el paquete IP usando la IP proporcionada por el usuario
    ip = IP(src=ip_cliente, dst="255.255.255.255")
    
    # Crear el paquete UDP
    udp = UDP(sport=68, dport=67)
    
    # Crear el paquete BOOTP con la dirección MAC del cliente
    bootp = BOOTP(op=1, chaddr=mac2str(mac_cliente))  # Convertir la cadena MAC a formato bytes
    
    # Crear el paquete DHCP Discover con opciones
    dhcp = DHCP(options=[
        ("message-type", "discover"),
        ("client-id", mac_cliente),  # Identificación del cliente
        ("requested-address", ip_cliente),  # IP solicitada
        ("parameter-request-list", [
            "subnet-mask",
            "router",
            "domain-name-server"
        ]),
        ("end")
    ])
    
    # Unir todos los paquetes
    paquete = eth / ip / udp / bootp / dhcp
    
    # Mostrar el contenido del paquete
    paquete.show()

    # Enviar el paquete DHCP Discover
    sendp(paquete, iface="eno1")

    # Escuchar por respuestas DHCP
    respuesta = sniff(iface="eno1", filter="udp and (port 67 or port 68)", count=1, timeout=10)
    
    if respuesta:
        print("Respuesta del servidor DHCP:")
        respuesta.show()
    else:
        print("No se recibió respuesta del servidor DHCP.")

if __name__ == "__main__":
    # Pedir al usuario que ingrese la IP deseada
    ip_cliente = input("Introduce la dirección IP que deseas usar: ")
    
    enviar_paquete_dhcp_discover(ip_cliente)
