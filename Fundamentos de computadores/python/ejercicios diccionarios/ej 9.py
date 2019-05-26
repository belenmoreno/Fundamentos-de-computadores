#9
facturas = {}
pago_total = 0
cantidad_cobrada = 0
cantidad_pendiente = 0
añadir = "SI"

while añadir == "SI":
    numero_factura = int(input("que numero de factura es: "))
    coste_factura = float(input("cual es el coste de dicha factura: "))
    facturas[numero_factura] = coste_factura
    pago_total = pago_total + coste_factura
    pregunta = input("¿quieres seguir añadiendo (si)? ")
    añadir = pregunta.upper()
pagar = "PAGAR"
while pagar == "PAGAR":
    numero_facturas = int(input("¿que numero de factura quieres pagar? "))
    coste_factura = facturas.pop(numero_factura, 0)
    pregunta2 = input("¿quieres seguir pagando (pagar)? ")
    pagar = pregunta2.upper()
    cantidad_cobrada = cantidad_cobrada + coste_factura
    cantidad_pendiente = pago_total - cantidad_cobrada
print("la cantidad que falta por pagar es ", cantidad_pendiente)
print("la cantidad que ya se ha pagado ha sido ", cantidad_cobrada)
        
    