alumnos = ["juan", "pepe", "maria", "juancarlos", "paco", "candela"]
notas = []
for i in alumnos:
    calificacion = input(f"Que nota tiene {i}?")
    notas.append(calificacion)
print(f"{alumnos}")
print(f"{notas}")
