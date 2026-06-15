notas = []

notas.append(float(input("Ingresa tu nota de evaluacion N°1: ")))
notas.append(float(input("Ingresa tu nota de evaluacion N°2: ")))
notas.append(float(input("Ingresa tu nota de evaluacion N°3: ")))

nota1 = notas[0]
nota2 = notas[1]
nota3 = notas[2]

notafinal = ((nota1 * 0.40) + (nota2 * 0.40) + (nota3 * 0.40))

print("\n------NOTAS-------")
print(notas)
print("------------------")

print(f"\nEl promedio de tu notas de laboratorio es de un: {notafinal:.1f}")