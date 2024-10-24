monedas = {"Euros":"€","Dollar":"$","Yen":"Y"}
eleccion = input("¿Cual es tu divisa?: ")
if eleccion.capitalize() in monedas:
    print(f"{monedas.get(eleccion.capitalize())}")
else:
    print("Tu divisa no existe aqui")