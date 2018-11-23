salida = False
agenda = dict()

while not salida:

    accion = input("¿Que quieres hacer?" "[Añadir año de nacimiento [A] / Consultar año de nacimiento [C] / Salir[S]] : ")

    if accion == "A":
        print("Vas a añadir un año de nacimiento")
        print("---------------------------------")
        nombre = input("Nombre: ")
        año_nacimiento = input("Año de nacimiento: ")
        agenda[nombre] = año_nacimiento

    elif accion == "C":
        print("Vas a consutar el año de nacimiento de tu amigo")
        print("-----------------------------------------------")
        nombre = input("nombre de tu amigo: ")
        print(agenda[nombre])



    elif accion =="S":
        salida = True

