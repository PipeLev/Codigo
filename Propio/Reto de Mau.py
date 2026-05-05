#Menu
while True: #Dentro de un while doble tabulacion todo
    print("Menu")
    print("1.Hola")
    print("2.Mau")
    print("3.po")
    print("4.Salir")
    
    seleccion = input("Seleccione una opcion:")

    if seleccion == "1":
        print("Hola")
    elif seleccion == "2":
        print("Mau")
    elif seleccion == "3":
        print("po")
    elif seleccion == "4":
        print("saliendo...")
        break #dejarlo despues de la ultima opcion