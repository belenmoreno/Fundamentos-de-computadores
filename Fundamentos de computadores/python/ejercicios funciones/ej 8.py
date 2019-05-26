def muestra(numeros):
    operaciones = {}
    operaciones['media'] = sum(numeros)/len(numeros)
    operaciones['varianza'] = sum((numeros))/len(numeros)-numeros['media']**2
    operaciones['desviacion tipica'] = numeros['varianza']**0.5
    return numeros

print(muestra([1, 2, 3, 4, 5])) 