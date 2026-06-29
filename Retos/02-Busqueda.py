conceptos_repetidos = ['inmutable', 'iterable', 'inmutable', 'hashable', 'interpretado', 'iterable']


conceptos_limpios = sorted(set(conceptos_repetidos))

print("Conceptos sin duplicados (ordenados):")
print(conceptos_limpios)
print("-" * 60)


glosario = {
    'hashable': 'Objeto cuyo valor hash nunca cambia y puede ser clave.',
    'inmutable': 'Objeto con un valor fijo que no se puede modificar.',
    'interpretado': 'Lenguaje donde el código se ejecuta línea a línea.',
    'iterable': 'Objeto capaz de devolver sus elementos uno a la vez.'
}

print("Glosario construido:")
for concepto, definicion in glosario.items():
    print(f"  - {concepto}: {definicion}")
print("-" * 60)

concepto_buscado = input("Ingrese el concepto que desea buscar: ").strip().lower()


if concepto_buscado in glosario:
    definicion_encontrada = glosario[concepto_buscado]
    print(f"Resultado de la búsqueda -> {concepto_buscado}: {definicion_encontrada}")
else:
    definicion_encontrada = None
    print("El concepto ingresado no se encuentra en el glosario.")
print("-" * 60)

if definicion_encontrada is not None:
    registro_busqueda = (concepto_buscado, definicion_encontrada)
    print("Registro inmutable de la consulta:")
    print(registro_busqueda)
else:
    print("No se generó un registro porque el concepto no existe en el glosario.")