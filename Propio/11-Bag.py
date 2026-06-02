#System at bag
bag = []

seleccion = 1 
while seleccion == 1:
    bag.append(input("\nIngresa los items para la mochila: "))

    print("Se guardo correctamente el Item")

    print("\n-----------------------------------")

    print("\n¿Deseas agregar algo mas a la mochila?")
    print("1.- SI")
    print("2.- NO")

    seleccion = int(input("\nIngresa la Opcion: "))

    if seleccion == 2:
        print("Saliendo de la Mochila...")
        break

print("\n¿Deseas ver los items guardados?")
print("1.- SI")
print("2.- NO")

seleccion2 = int(input("Seleccione la opcion a operar: "))

if seleccion2 == 1:
    print("\n-------------------BAG-------------------\n")
    print(bag)
else:
    print("No miras la mochila")

print("---------------------------------\n")

seleccion3 = 1

print("\n¿Quieres usar un item?")
print("1.- SI")
print("2.- NO")

seleccion4 = int(input("Seleccione una Opcion: "))

while seleccion3 == 1:
    if len(bag) == 0:
        print("\n te has quedado sin objetos")
        break

    if seleccion4 == 1:
        print("\n¿Qué ítem quieres usar?")
        
    for indice, item in enumerate(bag, start=1):
        print(f"{indice}.- {item}")
        
    opcion_item = int(input("\nIngresa el número del ítem a usar: ")) - 1
        
    if 0 <= opcion_item < len(bag):
        item_usado = bag.pop(opcion_item)
        print(f"\nVas a utilizar: {item_usado}")
        print(f"Mochila actualizada: {bag}")
    else:
        print("Selección inválida. Ese ítem no existe en la mochila.")

    print("\n¿Deseas usar otro item?")
    print("1.- SI")
    print("2.- NO")

    seleccion4 = int(input("Seleccione la opcion: "))

    if seleccion4 == 2:
        print("\nCerrando el programa...")
        break

print("\nGracias por usar el sistema :)")