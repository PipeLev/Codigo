Vendedores = {
    "Nino Nakano": [300000, 400000, 250000, 500000, 200000],  
    "Miku Nakano": [200000, 150000, 300000, 250000, 200000],  
    "Umi Asanagi": [100000, 120000, 90000, 110000, 80000]
}

SUELDO = 529000

print("----------REPORTE DE BONOS----------")

for nombre, ventas in Vendedores.items(): 
    
    total_ventas = sum(ventas) 
    promedio_ventas = total_ventas / len(ventas) 
    
    bono = 0
    if total_ventas > 1500000: 
        bono = SUELDO * 0.20 
    elif total_ventas > 1000000:
        bono = SUELDO * 0.10 
    elif total_ventas > 500000: 
        bono = SUELDO * 0.05 
    else:
        bono = 0
        
    sueldo_total = SUELDO + bono 
    
    print( f"Vendedora: {nombre}")
    print(f"  -> Total Ventas Semanal: ${total_ventas:,}") 
    print(f"  -> Promedio de Venta Diaria: ${promedio_ventas:,}") 
    print(f"  -> Bono Asignado: ${int(bono):,}") 
    print(f"  -> SUELDO TOTAL A PAGAR: ${int(sueldo_total):,}\n") 

print("----------------------------------------")

#Compañero Benjamin Bahamonde