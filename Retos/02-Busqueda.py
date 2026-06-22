#compañero Benjamin 
conceptos_repetidos = ["inmutable", "iterable", "inmutable", "hashable", "interpretado", "iterable"] #la lista

glosario = dict(
    Hashable = "Objeto cuyo valor hash nunca cambia y puede ser clave",
    Inmutable = "Objeto con un valor fijo que no se puede modificar",
    Interpretado = "Lenguaje donde el código se ejecuta línea a línea.",
    Iterable = "Objeto capaz de devolver sus elementos uno a la vez."
)

conceptos = []

while True:
    busqueda = input("Ingresa tu concepto que quieres buscar: ")
    for i in range(len(glosario)):
        match busqueda:
            case glosario[0]:
                print(glosario(0))
            case glosario(1):
                print(glosario(1))
            case glosario(2):
                print(glosario(2))
            case glosario(3):
                print(glosario(3))
            case None:
                print("un dato fue inresado incorrectamente")

