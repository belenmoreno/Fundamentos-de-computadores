#6
persona = {}
inombre = input("como te llamas: ")
persona['nombre'] = inombre
iedad = int(input("cuantos años tienes: "))
persona['edad'] = iedad
isexo = input("¿eres hombre o mujer? ")
persona['sexo'] = isexo
itelefono = int(input("cual es tu numero de telefono? "))
persona['telefono'] = itelefono
icorreo = input("cual es tu correo: ")
persona['correo'] = icorreo
print(persona)