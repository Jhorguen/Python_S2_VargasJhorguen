listaUsuarios = [{
    "nombre": "Jhorguen",
    "apellido": "Vargas",
    "edad": "20",
    "numero": "3043622663",
    "id": 23
}]

print(listaUsuarios[0]["nombre"] + " " + listaUsuarios[0]["apellido"])

booleano = True
while booleano:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Crear Persona")
    print("2. Mostrar todas las personas")
    print("3. Mostrar a una persona individual")
    print("4. Actualizar a una persona en específico")
    print("5. Eliminar a una persona en específico")
    print("6. Cerrar programa")
    try:
        opcionUsuario = int(input("Escoja una opción (Numérica): "))
    except ValueError:
        print("Entrada inválida. Debe ser un número.")
        continue

    if opcionUsuario == 1:
        print("Ingresa el nombre de la nueva persona a añadir")
        newName = input()

        print("Ingresa el apellido de la nueva persona a añadir")
        newLastName = input()

        print("Ingresa la edad de la nueva persona a añadir")
        newAge = input()

        print("Ingresa el número telefónico de la nueva persona a añadir")
        newNumber = input()

        print("Ingresa el ID de la nueva persona a añadir")
        try:
            newId = int(input())
        except ValueError:
            print("El ID debe ser un número.")
            continue

        newUser = {
            "nombre": newName,
            "apellido": newLastName,
            "edad": newAge,
            "numero": newNumber,
            "id": newId
        }

        listaUsuarios.append(newUser)
        print("--- DATOS DE LA NUEVA PERSONA AÑADIDA ---")
        print("Nombre:", newUser["nombre"])
        print("Apellido:", newUser["apellido"])
        print("Edad:", newUser["edad"])
        print("Número:", newUser["numero"])
        print("ID:", newUser["id"])

    elif opcionUsuario == 2:
        print("--- LISTADO DE TODAS LAS PERSONAS ---")
        for persona in listaUsuarios:
            print(persona)

    elif opcionUsuario == 3:
        print("¿Qué persona deseas ver? Ingresa el ID:")
        try:
            idBuscado = int(input())
        except ValueError:
            print("El ID debe ser un número.")
            continue

        encontrado = False
        for persona in listaUsuarios:
            if persona["id"] == idBuscado:
                print("Nombre:", persona["nombre"])
                print("Apellido:", persona["apellido"])
                print("Edad:", persona["edad"])
                print("Número:", persona["numero"])
                print("ID:", persona["id"])
                encontrado = True
                break

        if not encontrado:
            print("No se encontró ninguna persona con ese ID.")

    elif opcionUsuario == 4:
        print("Ingresa el ID de la persona a actualizar")
        try:
            idBuscado = int(input())
        except ValueError:
            print("El ID debe ser un número.")
            continue

        encontrado = False
        for persona in listaUsuarios:
            if persona["id"] == idBuscado:
                print("--- DATOS ACTUALES ---")
                print("Nombre:", persona["nombre"])
                print("Apellido:", persona["apellido"])
                print("Edad:", persona["edad"])
                print("Número:", persona["numero"])
                print("ID:", persona["id"])

                print("¿Qué dato desea actualizar?")
                print("1. Nombre")
                print("2. Apellido")
                print("3. Edad")
                print("4. Número")
                print("5. ID")
                try:
                    opcionActualizacion = int(input())
                except ValueError:
                    print("Entrada inválida.")
                    continue

                if opcionActualizacion == 1:
                    persona["nombre"] = input("Nuevo nombre: ")
                elif opcionActualizacion == 2:
                    persona["apellido"] = input("Nuevo apellido: ")
                elif opcionActualizacion == 3:
                    persona["edad"] = input("Nueva edad: ")
                elif opcionActualizacion == 4:
                    persona["numero"] = input("Nuevo número: ")
                elif opcionActualizacion == 5:
                    try:
                        persona["id"] = int(input("Nuevo ID: "))
                    except ValueError:
                        print("El ID debe ser numérico.")
                        continue
                else:
                    print("Opción no válida.")
                    continue

                print("--- DATOS ACTUALIZADOS ---")
                print("Nombre:", persona["nombre"])
                print("Apellido:", persona["apellido"])
                print("Edad:", persona["edad"])
                print("Número:", persona["numero"])
                print("ID:", persona["id"])
                encontrado = True
                break

        if not encontrado:
            print("No se encontró ninguna persona con ese ID.")

    elif opcionUsuario == 5:
        print("Ingrese el ID de la persona que desea eliminar:")
        try:
            idBuscado = int(input())
        except ValueError:
            print("El ID debe ser numérico.")
            continue

        encontrado = False
        for persona in listaUsuarios:
            if persona["id"] == idBuscado:
                listaUsuarios.remove(persona)
                print("Persona eliminada exitosamente.")
                encontrado = True
                break

        if not encontrado:
            print("No se encontró ninguna persona con ese ID.")

    elif opcionUsuario == 6:
        print("Gracias por usar el programa. ¡Hasta pronto!")
        booleano = False

    else:
        print("Opción inválida, por favor seleccione una opción del 1 al 6.")
