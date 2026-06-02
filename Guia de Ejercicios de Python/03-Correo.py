nombre = input("Ingresa tu nombre y apellido para generate el correo institucional: ")

nombre = nombre.lower()

nombre = nombre.strip()

nombre = nombre.replace(" ", ".")

print(f"Tu correo institucional es: {nombre}@alumnos.ulagos.cl")