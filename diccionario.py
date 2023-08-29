productoTerminado1={
    'referencia':5089,
    'marca': "Americanino",
    'descripcion': "chompa de acampar",
    'color': "naranja",
    'costo': 100000,
    'disponible': True,
    'costoVenta': 500000,
    'puntosVenta': ['cc mayorca', 'termina','puerta del norte']
}

productoTerminado2={
    'referencia':5088,
    'marca': "Americanino",
    'descripcion': "camiseta polo",
    'color': "azul oscuro",
    'costo': 200000,
    'disponible': True,
    'costoVenta': 400000,
    'puntosVenta': ['cc mayorca', 'termina','puerta del norte']
}

#creando una lista de diccionario
productos=[productoTerminado1, productoTerminado2]
#recorriendo una lista con ciclo for
'''for contador in range(1, 10, 2):
    print(contador)'''
for producto in productos:
    #print(producto["puntosVenta"])
    for puntoVenta in producto ["puntosVenta"]:
        print(puntoVenta)
    