categoria = []
gastos = []

while True:
    print("\n 1.Añadir gastos")
    print("\n 2.Mostrar gastos")
    print("\n 3.salir")
    opcion = int(input("que opcion eliges: "))
    if opcion == 1:
        new_product = input("Que gastos quires añadir?: ")
        if new_product in categoria:
            add_gastos = str(input("Este gasto ya existe ¿cuantos quieres añadir?: "))
            posicion = categoria.index(new_product)
            gastos[posicion] += add_gastos
        else:
            categoria.append(new_product)
            add_gastos = str(input("Cuantos quieres añadir?: "))
            gastos.append(add_gastos)
    elif opcion == 2:
        print("Mostrando gastos")
        print("-------------------")
        for i in range(0,len(categoria),1):
            print(f"{categoria[i]}: {gastos[i]}")
    elif opcion == 3:
        print("Saliendo.....")
        break
    else:
        print("Opcion incorrecta")