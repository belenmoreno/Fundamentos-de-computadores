tiempo = lambda minutos : minutos * 60
minutos = int(input("cuantos minutos quieres cambiar: "))
resul = tiempo(minutos)
print(resul)

tiempo = lambda minutos, seg : minutos * seg
#minutos = int(input("cuantos minutos quieres cambiar: "))
resul = tiempo(1200, 60)
print(resul)

tiempo = lambda minutos, seg : minutos * seg
minutos = int(input("cuantos minutos quieres cambiar: "))
resul = tiempo(minutos, 60)
print(resul)

