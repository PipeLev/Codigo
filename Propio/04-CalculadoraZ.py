num1 = int(input("Ingrese el primer digito:"))
num2 = int(input("Ingrese el segundo digito:")) 

resultado = num1 + num2

if num1 < 0 and num2 < 0: #si los 2 numeros son negativos
    print(f"El resultado de la suma de los numeros negativos de ({num1}) + ({num2}) es de: {resultado}")
elif num1 < 0 or num2 < 0: #si alguno de los 2 numeros es negativo se va a mostrar la resta
    print(f"El resultado de la resta de {num1} + {num2} es de: {resultado}")
else: #si los 2 numeros son positivos
    print(f"El resultado de la suma de {num1} + {num2} es de: {resultado}")