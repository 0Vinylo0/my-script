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
asistencia_alumnos = []
for i in lista:
    asistencia = input(f"{i} esta presente? ")
    asistencia_alumnos.append(asistencia)

i = 0
while (i < len(lista)):
    print(f"{lista[i]}{asistencia_alumnos}")
    i += 1