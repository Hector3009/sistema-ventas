DESCUENTO_MAXIMO = 10

def calcular_total(precio, descuento):
    if descuento < 0 or descuento > DESCUENTO_MAXIMO:
        return "Descuento no permitido"
    total = precio - (precio * descuento / 100)
    return round(total, 2)
