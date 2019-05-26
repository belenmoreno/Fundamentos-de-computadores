datos = {'Euro':'€', 'Dolar':'$', 'Yen':'y'}
pregunta = input("introduce una divisa: ")
print(datos.get(pregunta.title(), "no esta"))
