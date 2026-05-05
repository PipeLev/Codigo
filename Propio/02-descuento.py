precio = float(input("Ingresa el precio del producto: "))

descuento = float(input("Ingresa el porcentaje de descuento: "))

precio_final = precio - (precio * descuento / 100)

print(f"El precio final del producto con el descuento aplicado es: {precio_final}")