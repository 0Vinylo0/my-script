saldo = 50

while True:
    print("\n 1º-Consultar saldo")
    print("\n 2º-Recargar targeta")
    print("\n 3º-Hacer compra")
    print("\n 4º-Salir")
    
    opcion = int(input("Elige una opcion: "))

    if opcion == 1:
        print(f"Tienes {saldo}€ en la targeta")
    elif opcion == 2:
        catidad_añadir = int(input("¿Que cantidad quieres añadir a la targeta?: "))
        saldo =+ catidad_añadir
        print(f"Has añadido {saldo}€ a la targeta")
    elif opcion == 3:
        monto = int(input("¿De cuanto es la compra que quieres hacer?: "))
        if monto > saldo:
            print(f"Saldo insuficionetes tienes {saldo}€")
        else:
            saldo = saldo - monto
            print(f"Tu saldo es ahora es de {saldo}€")
    elif opcion == 4:
        print("Saliendo del programa...")
        break
    else:
        print("Opcion incorrecta...")