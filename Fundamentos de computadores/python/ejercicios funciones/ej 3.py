def factorial(positivo):
    numfactor = positivo
    for i in range(1, numentero, 1):
        numfactor = numfactor*i
    print("el numero factorial de ", positivo, "es ", numfactor)
    return

numentero = int(input("introduce un número entero: "))

factorial(numentero)