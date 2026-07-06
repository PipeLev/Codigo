mis_notas = [5.5, 5.5, 5.5, 5.5, 5.6]

print(f"La cantidad de notas es de: {len(mis_notas)}")

print("------------Notas--------------")
print(mis_notas)
print("-------------------------------")

print(f"La nota maxima fue de {max(mis_notas)} y la nota minima fue de {min(mis_notas)}")

promedio = (mis_notas[0] + mis_notas[1] + mis_notas[2] + mis_notas[3] + mis_notas[4]) / 5

print(f"El promedio final fue de un {promedio:.1f}")

