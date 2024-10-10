lista = ["pedro", "juan", "manolo"]
asistencia_alumnos = []
for i in lista:
    asistencia = input(f"{i} esta presente? ")
    asistencia_alumnos.append(asistencia)

i = 0
while (i < len(lista)):
    print(f"{lista[i]} {asistencia_alumnos[i]} esta presente")
    i += 1