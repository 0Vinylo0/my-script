saldo = 1000

while True:
    print("\n 1- Consultar saldo")
    print("\n 2- Retirar dinero")
    print("\n 3- Depositar dinero")
    print("\n 4- Salir")

    opcion = int(input("\n ¿Que accion deseas hacer?: "))
    
    if opcion == 1:
        print(f"Tines un saldo de {saldo}€")
    if opcion == 2:
        cantidad = int(input("¿Cuanto saldo quieres retirar?: "))
        if saldo < cantidad:
            print("Saldo insuficiente")
        else:
            saldo -= cantidad
    if opcion == 3:
        cantidad2 = int(input("¿Cuanto dinero quieres añadir?: "))
        saldo += cantidad2
    if opcion == 4:
        print("Hasta pronto :)")
        break