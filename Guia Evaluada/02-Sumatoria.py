num = 0

terminoA = 500
terminoB = 456  

print("Secuencia inicial: 500 + 456 + 510 + 454 + 520 + 452 + ... + 800")
while terminoA <= 800:
    num += terminoA
    
    if terminoA == 800:
        break
        
    num += terminoB

    terminoA += 10
    terminoB -= 2

print("\n-------------- Resultado ---------------")
print(f"La sumatoria total de la serie es: {num}")

#Compañero Benjamin Bahamonde