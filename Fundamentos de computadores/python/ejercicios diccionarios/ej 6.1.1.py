persona = {}
continua = "SI"
while continua == "SI":
    clave = input("¿qué dato quieres introducir? ")
    ivalor = input("introcuce el"+ clave) 
    persona[clave]  = ivalor
    print(persona)
    continua = input("¿quieres continuar? ")
    continua = continua.upper()


