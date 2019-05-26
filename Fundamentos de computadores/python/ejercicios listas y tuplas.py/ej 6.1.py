#6.1
asignaturas = ["mates", "física", "química", "historia", "lengua"]
listanotas = []
for asignatura in asignaturas:
    nota = input("¿que nota has sacado en " + asignatura + "? ")
    listanotas.append(nota)
for i in range(len(asignaturas)):
        print("he sacado un " + listanotas[i] + "en " + asignaturas[i])

