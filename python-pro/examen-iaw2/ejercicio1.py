producto = []
catidad = []

while True:
    print("\n 1º-Añadir Producto")
    print("\n 2º-Cambiar catidad de producto")
    print("\n 3º-Eliminar producto")
    print("\n 4º-Mostrar lsita de productos")
    print("\n 5º-Salir")
    opcion = int(input("Elige una opcion: "))
    if opcion == 1:
        producto_añadir = input("¿Que producto quieres añadir?: ")
        catidad_añadir = int(input("¿Que cantidad quieres añadir?: "))
        if producto_añadir in producto:
            print("¡Ese producto ya existe!")
        else:
            print(f"Añadiendo {producto_añadir} en la lista...")
            producto.append(producto_añadir)
            lugar_producto = producto.index(producto_añadir)
            catidad.insert(lugar_producto, catidad_añadir)
    elif opcion == 2:
        producto_cambiar = input("¿Que producto quieres cambiar?: ")
        if producto_cambiar in producto:
            cantidad_cambiar = input("¿Que cantidad quieres poner?: ")
            print("Cambiando cantidad...")
            lugar_producto_cambiar = producto.index(producto_cambiar)
            catidad.pop(lugar_producto_cambiar)
            catidad.insert(lugar_producto_cambiar, cantidad_cambiar)
        else:
            print("¡El producto idicado no existe!")
    elif opcion == 3:
        producto_eliminar = input("¿Que producto quieres eliminar?")
        if producto_eliminar in producto:
            print("Eliminando Producto...")
            lugar_producto_eliminar = producto.index(producto_eliminar)
            producto.pop(lugar_producto_eliminar)
            catidad.pop(lugar_producto_eliminar)
        else:
            print("¡El producto idicado no existe!")
    elif opcion == 4:
        for i in range(len(producto)):
            print(f"De {producto[i]} tienes {catidad[i]}")
    elif opcion == 5:
        print("Saliendo del programa...")
        break
    else:
        print("Opcion incorrecta...")