n = int(input("Ingresa la cantidad de cubos que deseas ver: "))

for fila in range(1, n + 1):
    primer_impar = fila * (fila - 1) + 1
    impares_fila = []
    
    for i in range(fila):
        siguiente_impar = primer_impar + (2 * i)
        impares_fila.append(siguiente_impar)
    
    suma_total = sum(impares_fila)
    texto_suma = " + ".join(str(num) for num in impares_fila)
    
    print(f"{fila}³ = {texto_suma} = {suma_total}")

#Compañero Benjamin Bahamonde