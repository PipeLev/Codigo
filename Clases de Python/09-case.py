print("Menu")
print("simplede 1 al 3")
print("9 para salir")

while True:
    opcion= input("Porfavor, elija una opcion de 1 al 3... ")
    match opcion:
        case "1":
            print("eleccion 1")
        case "2":
            print("eleccion 2")
        case "3":
            print("eleccion 3") 
        case "9":
            print("se rompio we")
            break