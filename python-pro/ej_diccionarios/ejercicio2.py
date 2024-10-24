datos = {}
nombre = datos["nombre"] = input("¿Cual es tu nombre?: ")
edad = datos["edad"] = input("¿Cual es tu edad?: ")
direccion = datos["direccion"] = input("¿Cual es tu direccion?: ")
telefono = datos["telefono"] = input("¿Cual es tu telefono?: ")

print(f"{datos['nombre']} tiene {datos['edad']} años, vive en {datos['direccion']} y su numero de telefono es {datos['telefono']}")