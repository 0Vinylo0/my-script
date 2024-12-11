kilos = float(input("¿Cual es tu peso en Kg?: "))
altura = input("¿Cual es tu altura en metros?: ")
altura_convertido = altura.replace(",", ".")

altura_cuadrado = float(altura_convertido) * float(altura_convertido)
indice = kilos / altura_cuadrado

if indice >= 18.5 and indice <=24.9:
    print(f"tu indice es de {indice}, es algo normal")
elif indice >= 25.0 and indice <= 29.9:
    print(f"tu indice es de {indice}, tienes sobrepeso")
elif indice >= 30:
    print(f"tu indice es de {indice}, tienes obesidad, deberias adelgazar")
elif indice <= 18.4:
    print(f"tu indice es de {indice}, estas muy delgado, come algo")