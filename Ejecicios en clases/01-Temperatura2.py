temperatura = [12.5, 14.2, 11.8]

resultado = round(sum(temperatura) / 3)

print(f"La temperatura maxima de la lista fue de {max(temperatura)}°C y La temperatura minima fue de {min(temperatura)}°C")
print(f"La diferencia entre los ellos es de {round(max(temperatura) - min(temperatura))}°C")
print(f"Y el promedio de las temperaturas de los tres dias es de {resultado}°C")