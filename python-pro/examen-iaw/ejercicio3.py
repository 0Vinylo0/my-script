tarjeta_saldo = float(20)
while True:
    print("\n 1-.Consultar saldo")
    print("\n 2-.Añadir saldo")
    print("\n 3-.Pago del billete (2.50€)")
    print("\n 4-.Salir")
    
    opcion = int(input("Selecciones una opcion: "))

    if opcion == 1:
        if float(tarjeta_saldo) > 2.50:
            print(f"Tu saldo actial es de {tarjeta_saldo}€")
        else:
            print(f"Saldo insuficiente para un billete, deberias recargar")
            print(f"{tarjeta_saldo}€")
    if opcion == 2:
        saldo_add = float(input("¿Cuanto saldo quieres añadir a la trajeta?: "))
        tarjeta_saldo += saldo_add
        print(f"{tarjeta_saldo}€")
    if opcion == 3:
        if float(tarjeta_saldo) < 2.50:
            print(f"No tienes saldo suficiente para comprar un billete, porfavor recarge su tarjeta.")
            print(f"{tarjeta_saldo}€")
        else:
            print("Gracias por confiar en nosotros, disfrute el viaje")
            tarjeta_saldo -= 2.50
            print(f"{tarjeta_saldo}")
    if opcion == 4:
        print("Gracias por confiar en nosotros, hasta pronto.")
        break
    if opcion > 4 or opcion < 1:
        print("¡Opcion incorrecta!")