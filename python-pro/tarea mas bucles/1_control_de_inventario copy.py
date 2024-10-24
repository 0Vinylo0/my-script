inventario = []
stock = []

while True:
    print("\n 1.Añadir producto")
    print("\n 2.Eliminar producto")
    print("\n 3.Mostrar producto")
    print("\n 4.salir")
    opcion = int(input("que opcion eliges: "))
    if opcion == 1:
        new_product = input("Que producto quires añadir?: ")
        if new_product in inventario:
            add_stock = int(input("Ese producto ya existe ¿cuantos quieres añadir?: "))
            posicion = inventario.index(new_product)
            stock[posicion] += add_stock
        else:
            inventario.append(new_product)
            add_stock = int(input("Cuantos quieres añadir?: "))
            stock.append(add_stock)
    elif opcion == 2:
        new_product = input("Que producto quieres eliminar: ")
        del_stock = int(input("Cuantos quieres eleiminar: "))
        if new_product in inventario:
            posicion = inventario.index(new_product)
            stock[posicion] -= del_stock
            if stock[posicion] < 0:
                stock[posicion] = 0
                
        else:
            print("Este producto no existe")
    elif opcion == 3:
        print("Mostrando productos")
        print("-------------------")
        for i in range(0,len(inventario),1):
            print(f"tenemos {stock[i]} de {inventario[i]}")
    elif opcion == 4:
        print("Saliendo.....")
        break
    else:
        print("Opcion incorrecta")