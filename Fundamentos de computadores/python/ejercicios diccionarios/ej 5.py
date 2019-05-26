#5
curso = {'mates':6, 'fisica':4, 'quimica':5}
creditos_totales = 0
for clave, valor in curso.items():
    print(clave, "tiene", valor, "creditos")
    creditos_totales = creditos_totales + valor
print("el numero total de creditos es ", creditos_totales)


