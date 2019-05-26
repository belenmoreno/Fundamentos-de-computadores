def factorial(positivo):
    numfactorial = positivo
    for i in range(1, numentero, 1):
        numfactorial = numfactorial*i
    print("el numero entero ", positivo, "es", numfactorial)
    return


numentero = int(input("introduce un numero entero positivo: "))

factorial(numentero)