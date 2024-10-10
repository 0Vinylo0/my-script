alumnos = ["juan", "pepe", "maria", "juancarlos", "paco", "candela"]
notas = []
for i in alumnos:
    calificacion = int(input(f"Que nota tiene {i}?"))
    notas.append(calificacion)
for i in alumnos:
    print(f"{i} tiene un {notas[len(i)]}")
suma_calificacion = 0
for i in range(len(alumnos)):
    suma_calificacion += notas[i]
print(f"Nota media es: {suma_calificacion / len(alumnos)}")