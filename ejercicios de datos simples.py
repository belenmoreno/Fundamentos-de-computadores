#ejercicios de datos simples
#1
#print("hola mundo!")

#2
#mensaje = "hola mundo!"
#print(mensaje)

#3
#name = "belen"
#print("hola", name, "!")

#4
#name = input("¿cual es tu nombre?")
#n = "6"
#print((name + "\n") * int(n))
    
#5
#name = "BELEN"
#n = "5"
#print(name, "tiene", n, "letras")
#print(name.upper())

#6
#print(((3+2)/(2*5))**2)

#7
#peso = input("¿cual es tu peso en kg?") 
#altura = input("¿cual es tu altura en metros")
#bmi = round(float(peso)/float(altura)**2,2)
#print("tu indice de masa corporal es " + str(bmi))

#8
#n = input("introduce un  numero entero: ")
#m = input("introduce un numero entero: ")
#print(n, "entre", m, "da un cociente", str(int(n)//int(m)), "y un resto", str(int(n)%int(m)))

#9
#cantidad = int(input("¿cual es tu cantidad a invertir?"))
#interes = int(input("¿cual es el interés anual?"))
#años = int(input("¿cual es el número de años?"))
#print("Capital final: " + str(round(cantidad * (interes / 100 + 1) ** años, 2)))

#10
contraseña = "buenosdias"
if contraseña == "buenosdias":
    print("contraseña correcta. ")
else:
    print("contraseña incorrecta. ")

#11
regalo = "zapatos"
if regalo == "zapatos":
    print("me lo quedo. ")
elif regalo == "zapatos feos":
    print("los cambio. ")
else:
    print("habrá que ver lo que es")


