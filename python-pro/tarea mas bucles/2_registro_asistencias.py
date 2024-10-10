lista = ["pedro", "juan", "manola"]
for i in range(0,len(lista),1):
    print(f"{lista[i]}")
    hola = input("presente, si o no: ")
    if hola == "si":
        lista[i] = lista[i] + ": presente"
    elif hola == "no":
        lista[i] = lista[i] + ": no presente"
print(f"{lista}")