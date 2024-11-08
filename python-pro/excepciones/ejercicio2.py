try:
    uno = float(input("Dame el primer numero a sumar: "))
    dos = (input("Dame el segundo numero a sumar: "))
    suma = uno + dos
    print(f"{suma}")
except TypeError:
    print("No se pueden sumar numeros con cadenas!!!!")
except ValueError:
    print("Dame numeros!!!!")