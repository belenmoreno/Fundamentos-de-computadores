n = int(input('introduce un numero entero enytre el 1 y el 10: '))
numero = 'tabla-' + str(n) + '.txt'
fnumero = open(numero, 'w')
for i in range(1, 11):
    fnumero.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n')
fnumero.close()

