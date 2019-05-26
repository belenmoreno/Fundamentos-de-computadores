numregalos = int(input("¿cuantos regalos tienes? "))
numbolsa = numregalos
for numbolsa in range(1, int(numregalos + 1), 1):
    regalo = input("¿que te han regalado?")
    print("te han regalado " + regalo)
    if regalo.upper() == "ZAPATOS":
     print("me lo quedo. ")
    elif regalo.upper() == "ZAPATOS FEOS":
     print("los cambio. ")
    elif regalo.upper() == "NIKI":
     print("me lo quedo también. ")
    else:
     print("habrá que ver lo que es")
print("mi amiga me ha regalado " + str(numregalos))