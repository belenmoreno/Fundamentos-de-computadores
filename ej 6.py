#6
numero = int(input("introduce un numero entero: "))
for i in range(numero):
    for j in range(i+1):
        print("*", end="")
    print("")