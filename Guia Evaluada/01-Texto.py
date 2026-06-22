try:
    parrafo = input("Ingrese el párrafo: ")
    
    if not parrafo.strip():
        raise ValueError("El texto no puede estar vacío")
        
    lista_palabras = parrafo.split()
    
    palabra_buscar = input("Ingrese la palabra a buscar: ")
    
    repeticiones = lista_palabras.count(palabra_buscar)
    
    print(f"La palabra '{palabra_buscar}' aparece {repeticiones} veces.")

except ValueError as e:
    print(f"Error: {e}")

#Compañero Benjamin Bahamonde