numero = int(input("introduce un numero entero: "))
for i in range(numero):
    for j in range(i+1):
        print(i, end=", ")
    print("")

numero = int(input("introduce un numero: "))
for i in range(1, numero+1, 1):
    for j in range(i+1):
        print(j, end=", ")
    print("")
