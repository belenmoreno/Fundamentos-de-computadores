def factura(total):
    iva = total*0.21
    solucion = total+iva
    print("la cantidad de dinero introducida ", total , "es ", solucion , "con el iva.")
    return



cantidad = float(input("introduce la cantidad de dinero: "))
factura(cantidad)