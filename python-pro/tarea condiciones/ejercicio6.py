numeros_usuario = int(input("Dame un numero: "))

numeros_usuario %= 2

if numeros_usuario == 0:
    print("tu nuemro es par")

elif numeros_usuario == 1:
    print("tu numero es impar")