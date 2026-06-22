import time

for hora in range(24):
    for minutos in range(60):
        for segundos in range(60):
            
            print(f"Hora {hora:02d}, Minutos {minutos:02d}, Segundos {segundos:02d}", end="\r")
            
            
            time.sleep(1)
#Compañero Benjamin Bahamonde