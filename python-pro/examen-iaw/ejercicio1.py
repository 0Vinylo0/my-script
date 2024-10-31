tarea = []
prioridad = []
while True:
    print("\n 1-.Añadir tarea")
    print("\n 2-.Cambiar prioridad de la tarea")
    print("\n 3-.Eliminar tarea")
    print("\n 4-.Mostrar lista de tareas")
    print("\n 5-.Salir")
    
    opcion = int(input("Selecciones una opcion: "))

    if opcion == 1:
        nombretarea = (input("¿Que tarea quieres añadir?: "))
        if nombretarea in tarea:
            print("Esa tarea ya existe, no se añadira la tarea")
        else:
            prioridad_add = ((input("¿Que prioridad tiene esta tarea?(alta | media | baja): ")))
            print("Añadiendo tarea ...")
            tarea.append(nombretarea)
            posicion_nombre_tarea = tarea.index(nombretarea)
            prioridad.insert(posicion_nombre_tarea, prioridad_add)
    if opcion == 2:
        tarea_edid_prioridad = input("¿Que tarea quieres cambiar de prioridad?: ")
        if tarea_edid_prioridad in tarea:
            prioridad_edit = input("¿Que prioridad quieres ponerle?(alta | media | baja): ")
            posicion_edit_tarea = tarea.index(tarea_edid_prioridad)
            prioridad.pop(posicion_edit_tarea)
            prioridad.insert(posicion_edit_tarea, prioridad_edit)
        else:
            print("Esa tarea no existe")
    if opcion == 3:
        if len(tarea) == 0 and len(prioridad) == 0:
            print("Esa tarea no existe")
        else:
            tarea_del = input("¿Que tarea desea eliminar?: ")
            if tarea_del in tarea:
                posicion_del_tarea = tarea.index(tarea_del)
                tarea.remove(tarea_del)
                prioridad.pop(posicion_del_tarea)
            else:
                print("Esa tarea no existe")
    if opcion == 4:
        if len(tarea) == 0 and len(prioridad) == 0:
            print("No hay ninguna tarea, si quieres puedes añadir una")
        else:
            for i in range(len(tarea)):
                print(f"- {tarea[i]} prioridad {prioridad[i]}")
    if opcion == 5:
        print("Gracias por su apoyo, hasta pronto :-)")
        break
    if opcion > 5 or opcion < 1:
        print("¡Opcion incorrecta!")