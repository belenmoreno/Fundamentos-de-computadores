nombre = input("¿cual es tu nombre?")
sexo = input("¿cual es tu sexo (H o M)?")
if sexo == "M":
    if nombre < "m":
        print("GRUPO A")
    else:
        print("GRUPO B")
else:
    if nombre > "n":
        print("GRUPO A")
    else:
        print("GRUPO B")
    