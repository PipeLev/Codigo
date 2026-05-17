import random
n = random.randrange(120)
print(f"Numero elegido {n}")

if n < 10:
    print(f"el numero {n} es menor de 10")
elif n > 50:
    print(f"el numero {n} es mayor a 50")
elif n == 120:
    print (f"{n} es el numero maximo")
elif n == 0:
    print (f"no hay nada")