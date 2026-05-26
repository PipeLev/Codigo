consumo = []

consumo.append(float(input("Ingresa el consumo de la RAM en la mañana: ")))
consumo.append(float(input("Ingresa el consumo de la RAM en el medio dia: ")))
consumo.append(float(input("Ingresa el consumo de la RAM en la tarde: ")))
consumo.append(float(input("Ingresa el consumo de la RAM en la noche: ")))

mañana = consumo[0]
mediodia = consumo[1]
tarde = consumo[2]
noche = consumo[3]

consumo_total = (mañana + mediodia + tarde + noche) / 4 

print(f"El consumo de la Memoria RAM del servido durante el dia fue de {consumo_total} GB")

print(f"La diferencia de consumo entre {max(consumo)} GB y de {min(consumo):} GB es de: {max(consumo) - min(consumo)} GB de memoria RAM")