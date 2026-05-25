anchura = int(input("Anchura de tu rectángulo: "))
altura = int(input("Altura de tu rectángulo: "))

for i in range(altura):
    for j in range(anchura):
        print("* ", end="")
    print()