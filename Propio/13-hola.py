import pandas as pd

Datos = {"Mes" : ["Enero", "Febrero", "Marzo", "Abril"], "Gasto" : [10000, 15000, 7000, 5000], "Ventas" : [20000, 40000, 30000, 15000]}
contabilidad = pd.DataFrame(Datos)
print(contabilidad) 