def libras(importe, cotizacion):
    importelibras = importe*cotizacion
    print("el importe de ", importe, "euros son ", importelibras, "libras")
    return

    
cantidad = int(input("¿que valor quieres convertir a libras? "))
saldo = float(input("¿cuanto saldo tienes? "))
debe = float(input("¿cual es tu debe? "))
haber = float(input("¿cual es tu haber? "))
cotizadia = float(input("¿cual es la cotización euro-libra? "))

libras(cantidad, cotizadia)
libras(saldo, cotizadia)
libras(debe, cotizadia)
libras(haber, cotizadia)
