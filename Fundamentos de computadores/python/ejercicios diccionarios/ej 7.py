#7
cesta = {}
continuar = "SI"
costetotal = 0
while continuar == "SI":
    articulo = input("¿que quieres comprar? ")
    precio = float(input("¿cuanto cuesta? "))
    cesta[articulo] = precio
    print(cesta)
    continuar = input("¿quieres continuar? ")
    continuar = continuar.upper()
print("lista de la compra: ")
for articulo, precio in cesta.items():
    print(articulo, precio)
    costetotal = costetotal + precio
print("coste total: ", costetotal)



