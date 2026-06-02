tiempos_respuesta = []

tiempos_respuesta.append(float(input("Ingresa el tiempo de respuesta N°1: ")))
tiempos_respuesta.append(float(input("Ingresa el tiempo de respuesta N°2: ")))
tiempos_respuesta.append(float(input("Ingresa el tiempo de respuesta N°3: ")))

brecharendimiento = max(tiempos_respuesta) - min(tiempos_respuesta)
promedio = (tiempos_respuesta[0] + tiempos_respuesta[1] + tiempos_respuesta[2]) /3

print("\n------LISTA DE VELOCIDAD-------")
print(tiempos_respuesta)
print("\n-------------------------------")

print(f"La velocidad maxima de tiempo de respuesta fue de {max(tiempos_respuesta)} ms Y el tiempo minimo fue de {min(tiempos_respuesta)} ms")

print(f"La velocidad promedio fue de {round(promedio, 2)} ms")

print(f"La brecha de rendimiento fue de {round(brecharendimiento, 2)} ms")