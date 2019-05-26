#8
diccionario = {}
continuar = "SI"
while continuar == "SI":
    español = input("introduce una palabra en español: ")
    ingles = input("ahora introduce la misma en ingles: ")
    diccionario[español] = ingles
    continuar = input("¿quieres continuar? ")
    continuar = continuar.upper()
    print(diccionario)
pregunta = input("Introduce una frase para traducirla: ")
for español, ingles in diccionario.items():
    pregunta = ingles
print(pregunta)