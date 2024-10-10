alumnos = ["juan", "pepe", "maria", "juancarlos", "paco", "candela"]
notas = []
for i in alumnos:
    calificacion = int(input(f"Que nota tiene {i}?"))
    notas.append(calificacion)
contador = 0
for i in alumnos:
    print(f"{i} tiene un {notas[contador]}")
    contador += 1
suma_calificacion = 0
for i in range(alumnos):
    suma_calificacion += notas[i]
print(f"Nota media es: {suma_calificacion / alumnos}")