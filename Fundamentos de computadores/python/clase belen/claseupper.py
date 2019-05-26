
regalo = input("¿que te han regalado?")
print("te han regalado " + regalo)
if regalo.upper() == "ZAPATOS":
    print("me lo quedo. ")
elif regalo.upper() == "ZAPATOS FEOS":
    print("los cambio. ")
else:
    print("habrá que ver lo que es")

print("te recuerdo que son " + regalo)
print("aunque en el programa he comparado con " + regalo.upper())