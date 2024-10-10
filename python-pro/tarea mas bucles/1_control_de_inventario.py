while True:
    print("\n 1.Añadir producto")
    print("\n 2.Eliminar producto")
    print("\n 3.Mostrar producto")
    print("\n 4.salir")
    opcion = int(input("que opcion eliges: "))
    if opcion == 1:
        print("Que producto quires añadir: ")
    elif opcion == 2:
        print("Que producto quieres eliminar: ")
    elif opcion == 3:
        print("Mostrando productos")
        print("-------------------")
    elif opcion == 4:
        print("Saliendo.....")
        break
    else:
        print("Opcion incorrecta")