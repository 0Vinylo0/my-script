articulos_precios = {"Lapiz": 0.50,"Cuaderno" : 1.20,"Boligrafo" : 0.75,"Borrador" : 0.30}
while True:
    print("\n Bienvenido a la tienda")
    print("\n ----------------------")
    articulo = str(input("Introduce nombre del artuculo: "))
    if articulo in articulos_precios:
        catidad = float(input("Introduce cantidad deseada: "))
        precio_articulo = articulos_precios.get(articulo)
        print(f"El costo total de {catidad} {articulo} es de: {catidad * precio_articulo}")
    else:
        print("Articulo no disponible en la tienda")