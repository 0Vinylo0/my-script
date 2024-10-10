inventario = []
stock = []

while True:
    print("\n 1.Añadir producto")
    print("\n 2.Eliminar producto")
    print("\n 3.Mostrar producto")
    print("\n 4.salir")
    opcion = int(input("que opcion eliges: "))
    if opcion == 1:
        new_product = input("Que producto quires añadir: ")
        for i in inventario:
            if (new_product == i):
                print(f"{new_product} ya existe")
                add = input("Cuantos quieres añadir: ")
                stock[i].append(new_product)
            else:
                inventario.append(new_product)
                add = input("Cuantos quieres añadir: ")
                stock[i].append(new_product)
    elif opcion == 2:
        print("Que producto quieres eliminar: ")
    elif opcion == 3:
        print("Mostrando productos")
        print("-------------------")
        print(f"{inventario}")
    elif opcion == 4:
        print("Saliendo.....")
        break
    else:
        print("Opcion incorrecta")