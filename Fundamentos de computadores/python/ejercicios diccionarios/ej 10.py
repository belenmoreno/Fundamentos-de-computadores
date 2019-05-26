#10
clientes = {}
datos = "SI"
while datos == "SI":
    dni = (input("introduce tu DNI: "))
    nombre = input("introduce tu nombre: ")
    direccion = input("introduce tu direccion ")
    telefono = int(input("introduce tu numero de telefono: "))
    correo = input("introduce tu correo: ")
    preferente = input("¿eres cliente preferente si o no? ")
    cliente = {'nombre': nombre, 'direccion': direccion, 'telefono': telefono, 'correo': correo, 'preferente': preferente== "si"}
    clientes[dni] = cliente
    continuar = input("¿quieres continuar introduciendo datos (si)?")
    datos = continuar.upper()
datos2 = "CONTINUAR"
while datos2 == "CONTINUAR":
    dni = (input("introduce tu DNI: "))
    #if dni in clientes:
        #del clientes[dni]
    cliente = clientes.pop(dni, 0)
    continuar2 = input("¿quieres continuar preguntando el dni de tus clientes (continuar)? ")
    datos2 = continuar2.upper()
datos3 = "SEGUIR"
while datos3 == "SEGUIR":
    dni = (input("introduce tu DNI: "))
    for dni, cliente in clientes.items():
        print(dni, ": ", cliente)
    continuar3 = input("¿quieres seguir (seguir)? ")
    datos3 = continuar3.upper()
datos4 = "MOSTRAR"
while datos4 == "MOSTRAR":
    dni = (input("introduce tu DNI: "))
    for dni, cliente in clientes.items():
        print(dni, cliente[nombre])
    continuar4 = input("¿quieres continuar (mostrar)? ")
    datos4 = continuar4.upper()







    
