alumnos = ["juan", "pepe", "maria", "juancarlos", "paco", "candela"]
notas = []
for i in alumnos:
    calificacion = input(f"Que nota tiene {i}?")
    notas.append(calificacion)
for i in alumnos:
    print(f"{i} tiene un {notas[len(i)]}")