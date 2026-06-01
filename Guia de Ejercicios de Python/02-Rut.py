rut = " 19.543.872-K "

print(f"Este sistema es para tener en limpio un rut como por ejemplo: {rut}")

rut = rut.strip()

rut = rut.replace(".", "")

print(f"La longitud del RUT es de: {len(rut)} Caracteres Y el RUT en limpio seria asi: {rut}")