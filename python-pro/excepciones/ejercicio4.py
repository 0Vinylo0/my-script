lista = ([0,1,2,3])
while True:
    try:
        numero_lista = int(input("Dame un numero del 0 al 3: "))
        numero_a_dividir = float(input("Dame un numero para dividir: "))
        divide = numero_a_dividir / lista[numero_lista]
        print(f"{divide}")
        break
    except ValueError:
        print("Dame un numerito guapo ;)")
    except IndexError:
        print("Dame un numero dentro de la lista :(")
    except ZeroDivisionError:
        print("No me dividas entre zero guapo")
    except EOFError and KeyboardInterrupt:
        print("")
        print("Saliendo del programa...")
        break