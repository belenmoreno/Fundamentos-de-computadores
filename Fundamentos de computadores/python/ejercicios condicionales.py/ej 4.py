edad = int(input("¿cuantos años tienes?"))
ingresos = int(input("¿cuales son tus ingresoso?"))
if edad < 16:
    print("no puede tributar")
elif ingresos < 1000:
    print("no puede tributar")
else: 
    print("puede tributar. ")
