alumnos = ["juan", "pepe", "maria", "juancarlos", "paco", "candela"]
notas = []
for i in alumnos:
    calificacion = input(f"Que nota tiene {i}?")
    notas.append(calificacion)
contador = 0
for i in alumnos:
    print(f"{i} tiene un {notas[contador]}")
    contador += 1