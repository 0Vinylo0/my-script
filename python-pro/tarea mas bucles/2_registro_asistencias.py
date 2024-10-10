#lista = ["pedro", "juan", "manola"]
#for i in range(0,len(lista),1):
#    print(f"{lista[i]}")
#    hola = input("presente, si o no: ")
#    if hola == "si":
#        lista[i] = lista[i] + ": presente"
#    elif hola == "no":
#        lista[i] = lista[i] + ": no presente"
#print(f"{lista}")

lista = ["pedro", "juan", "manolo"]
for i in lista:
    print(f"{i}")
    input("presente, si o no: ")
    if i == "si":
        lista.append(f"{i}: presente")
    elif i == "no":
        lista.append(f"{i}: no presente")
print (f"{i}")