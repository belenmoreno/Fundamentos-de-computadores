#3
asignaturas = ["mates", "fisica", "quimica", "historia", "lengua"]
listanotas = []
for asignatura in asignaturas:
    nota = input("¿que nota has sacado en " + asignatura + "? ")
    listanotas.append(nota)
numasignaturas = len(asignaturas)
for i in range(numasignaturas):
    print("en", asignaturas[i] , "has sacado un" , listanotas[i] , sep=' ', end= "\n")


#3.1
comidas = ["pasta", "verduras", "fruta", "leche", "agua", "chuches"]
kilos = []
for comida in comidas:
  compra = (input("¿cuantos kilos quieres comprar en " + comida + "? "))
  kilos.append(compra)
for i in range(len(comidas)):
  print("tengo que comprar " + kilos[i] + " kilos " + "de " + comidas[i])
