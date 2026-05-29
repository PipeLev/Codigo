tramo1 = 50 + 30j
tramo2 = 40 - 10j

print(f"Este sistema sirve para hacer el calculo de los tramos {tramo1} y {tramo2}")

print(f"El Calculo Total de los 2 tramos de Fibra Optica es de {tramo1 + tramo2}")

print(f"La parte real (resistencia) es de: {int((tramo1 + tramo2).real)}")

print(f"La parte imaginaria (reactancia) es de: {int((tramo1 + tramo2).imag)}")