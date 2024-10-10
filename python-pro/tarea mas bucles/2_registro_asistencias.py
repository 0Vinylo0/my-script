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
    alumno = i
    print(f"{alumno}")
    input("presente, si o no: ")
    if alumno == "si":
        lista.append(f"{alumno}: presente")
    elif alumno == "no":
        lista.append(f"{alumno}: no presente")
print (f"{alumno}")