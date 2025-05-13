listaUsuarios = [{"nombre":"Jhorguen", 
                  "apellido"  :"Vargas",
                  "edad": "20",
                  "numero": "3043622663",
                  "id":23}]

print(listaUsuarios[0]["nombre"]+" "+ listaUsuarios[0]["apellido"])


print("1. Crear Persona")
print("2. Mostrar todas las personas")
print("3. Mostrar a una persona individual")
print("4. Actualizar a una persona en específico")
print("5. Eliminar a una persona en específico")
print("6. Cerrar programa")

opcionUsuario=int(input("Escoja una opción (Numérica):"))

if(opcionUsuario==1):
    print("Ingresa el nombre de la nueva persona a añadir")
    newName=input()

    print("Ingresa el apellido de la nueva persona a añadir")
    newLastName=input()

    print("Ingresa la edad de la nueva persona a añadir")
    newAge=int(input())

    print("Ingresa el numero telefonico de la nueva persona a añadir")
    newNumber=int(input())

    print("Ingresa el ID de la nueva persona a añadir")
    newId=int(input())

    newUser= {"nombre":newName, 
                "apellido"  :newLastName,
                "edad": newAge,
                "numero": newNumber,
                "id": newId}
    
    print("-------------------------------")
    print("---DATOS DE LA NUEVA PERSONA---")
    print("Nombre:", newUser["nombre"])
    print("Apellido:", newUser["apellido"])
    print("Edad:",newUser["edad"])
    print("Numero:",newUser["numero"])
    print("ID:",newUser["id"])
    print("----------------------------------")
    listaUsuarios.append(newUser)
    
elif(opcionUsuario==2):
    print("-------------------------------")
    print("---Listado de todas las personas---")
    print(listaUsuarios)
    print("----------------------------------")


elif(opcionUsuario==3):
    print("¿Qué persona deseas ver?, Ingresa el ID de la persona")
    idBuscado = int(input())

    encontrado = False
    for persona in listaUsuarios:
        if persona["id"] == idBuscado:
            print("Nombre:", persona["nombre"])
            print("Apellido:", persona["apellido"])
            print("Edad:", persona["edad"])
            print("Número:", persona["numero"])
            print("ID:", persona["id"])
            encontrado = True

    if not encontrado:
        print("No se encontró ninguna persona con ese ID.")

elif(opcionUsuario==4):
    print("Ingresa el ID de la persona a actualizar")
    idBuscado = int(input())

    encontrado = False
    for persona in listaUsuarios:
        if persona["id"] == idBuscado:
            print("Nombre:", persona["nombre"])
            print("Apellido:", persona["apellido"])
            print("Edad:", persona["edad"])
            print("Número:", persona["numero"])
            print("ID:", persona["id"])
            print("-------------------------------")
            print(" ")
            print("Que datos desea actualizar?(Opcion numerica)")
            print("1.nombre 2.apellido 3.edad 4.numero 5.ID")
            opcionActializacion = int(input())

            if(opcionActializacion==1):
                print("Ingresa el nuevo nombre:")
                persona["nombre"] = input()

            elif(opcionUsuario==2):
                print("Ingresa el nuevo apellido:")
                persona["apellido"] = input()

            elif(opcionUsuario==3):
                print("Ingresa la nueva edad:")
                persona["edad"] = input()
                
            elif(opcionUsuario==4):
                print("Ingresa el nuevo numero:")
                persona["numero"] = int(input())

            else:
                print("Escoge una opcion de actulizacion de datos correcta!")

            print("-----DATOS ACTUALIZADOS-----")
            print("Nombre:", persona["nombre"])
            print("Apellido:", persona["apellido"])
            print("Edad:", persona["edad"])
            print("Número:", persona["numero"])

            
        encontrado = True

    if not encontrado:
        print("No se encontró ninguna persona con ese ID.")



