#word = input ("introduce palabra:")
#for i in range(10):
#    print (word)

#ejercicio 2
#age = int(input("¿cuantos años tienes?"))
#for i in range(age):
    #print("has cumplido " + str(i+1) + " años")

#ejercicio 3
#n = int(input("introduce un número entero positivo: "))
#for i in range(1, n+1, 2):
    #print(i, end=", ")

#ejercicio 4
#n = int(input("introduce un numero entero positivo: "))
#for i in range(n , -1, -1):
#    print(i, end=", ")

#ejercicio 5
amount = float(input("¿cantidad a invertir "))
interest = float(input("interés porcentual anual "))
years = int(input("¿años"))
for i in range(years):
    amount *= 1 +interest / 100
    print("capital tras " + str(i+1) + " años: " + str(round(amount, 2)))
    
name  = "belen"
print("hola " + name)
