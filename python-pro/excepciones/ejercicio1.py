try:
    uno = float(input("Dame el primer numero: "))
    dos = float(input("Dame el segundo numero: "))
    divide = uno/dos
    print(f"{divide}")
except ZeroDivisionError:
    print("No me dividas entre cero amigo eso da infinito :(")
except ValueError:
    print("Dame numeros validos o pon numeros")