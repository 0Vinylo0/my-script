lista = [1,2,3,4]
try:
    numero_lista = int(input("Dame un numero del 0 al 3 "))
    print(f"{lista[numero_lista]} felicidades no fallaste")
except ValueError:
    print("Dame un numerito guapo ;)")
except IndexError:
    print("Fallaste ese numero no esta dentro :(")