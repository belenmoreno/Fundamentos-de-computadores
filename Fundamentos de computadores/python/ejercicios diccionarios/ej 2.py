#2
nombre = input("¿como te llamas? ")
edad = int(input("¿cuantos años tienes? "))
direccion = input("¿donde vives? ")
telefono = int(input("¿cual es tu numero de tlf? "))
persona = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}
print(persona['nombre'], " tiene ", persona['edad'], " y vive en ", persona['direccion'], " y su numero de tlf es ", persona['telefono'])