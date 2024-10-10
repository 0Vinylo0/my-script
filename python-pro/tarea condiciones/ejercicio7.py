edad = int(input("¿cual es tu edad?: "))
ingresos = int(input("¿cuanto cobras?: "))

if (edad > 16) and (ingresos >= 1000):
    print("a pagar a pagar, jijijijijiji")

elif (edad <= 16) and (ingresos < 1000):
    print("ninguno de los dos loco que cojones XD")

elif (edad < 17):
    print("te falta poco")

elif (ingresos < 1000):
    print("no tiene iphone, pobre")