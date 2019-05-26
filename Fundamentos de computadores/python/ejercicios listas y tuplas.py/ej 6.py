#6
asignaturas = ["mates", "física", "química", "historia", "lengua"]
aprobadas = []
for asignatura in asignaturas:
    nota = float(input("¿que nota has sacado en " + asignatura + "? "))
    if nota >= 5:
        aprobadas.append(asignatura)
for asignatura in aprobadas:
    asignaturas.remove(asignatura)
print("tienes que repetir" + str(asignaturas))