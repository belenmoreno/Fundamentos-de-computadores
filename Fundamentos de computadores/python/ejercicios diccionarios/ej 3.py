#3
compra = {'Platano':1.35, 'Manzana':0.80, 'Pera':0.85, 'Naranja': 0.70}
fruta = input("¿que fruta quieres comprar? ").title()
kilos = float(input("¿cuantos kilos de fruta quieres comprar? "))
if fruta in compra:
    print(kilos , "de ", fruta, "valen", compra[fruta]*kilos)
else:
    print("lo siento ", fruta, "no esta. ")