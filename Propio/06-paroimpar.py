# Asumimos que 'seleccion' se define con 1 inicialmente para entrar al flujo
seleccion = 1

while seleccion == 1:
    num1 = int(input("Ingrese su numero para saber si es par o impar: "))

    if num1 % 2 == 0:
        print("Es par")
    else:
        print("Es impar")
    
    # Preguntamos dentro del bucle si quiere continuar
    print("\n¿Deseas saber otro numero?")
    print("1. Si")
    print("2. No")
    seleccion = int(input("Seleccione una opción: "))

if seleccion == 2:
    print("Cerrando...")