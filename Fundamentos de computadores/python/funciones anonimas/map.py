tiempo = lambda minutos : minutos * 60
minutos = int(input("cuantos minutos quieres cambiar: "))
resul = tiempo(minutos)
print(resul)

lista = list(map(tiempo, [minutos, 100, 824]))
print(lista)