precios = {"Platano":1.35, "Manzana":0.80, "Pera":0.85, "Naranja":0.70}
fruta = input("Que fruta quieres: ")
if fruta.capitalize() in precios:
    kilos = float(input("Cuantos kilos: "))
    print(f"Las {fruta.capitalize()} estan a {precios.get(fruta.capitalize())} a si que el total es {precios.get(fruta.capitalize())*kilos}")
else:
    print(f"Ese tal {fruta} no se vende aqui !Fuera¡")