paciente = dict(
    nombre = "daniela",
    edad = 18,
    ciudad = "castro",
    fecha_de_ingreso = "18-abril-2026",
    motivo_de_ingreso = "dolor en el pie"
)

texto = ["nombre", "edad", "ciudad", "fecha de ingreso", "motivo de ingreso"]

for i in range (len(paciente)):
    pocision = texto[i].replace(" ", "_")
    print(f"\n {texto[i]}: {paciente[pocision]}")