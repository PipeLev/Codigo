edad = 15
num = 0

#while edad < 18:
    #print("menor de edad")

#while True:
    #print(num)
    #num = num + 2

while num <= 100:
    print(num)
    num = num + 2
print("1°bucle")




while num <= 200:
    print(num)
    num = num + 2
else:
    print("es igual o mayor a 200")
print("2°bucle")


while num <= 300:
    print(num)
    num = num + 2
    if num == 250:
        print("es igual a 250")
print("3°bucle")


while num <= 400:
    print(num)
    num = num + 2
    if num == 350:
        print("break")
        break
print("4°bucle")

num = 0
#continue
while num < 50:
    num = num + 1
    if num == 40:
        continue
    print(num)

print("----for-----")
for i in (1,2,3,4,5,6,7,8,9,10):
    print(i)

listita = [1,2,3,4,5,6,7,8,9,10]

print("------lista----")
for n in listita:
    print(n)

print("range")
for b in range(1,101,2):
    print(b)