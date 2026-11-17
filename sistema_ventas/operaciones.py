def calcular_total(ventas):
    total = 0 
    i = 0

    while i < len(ventas):
        total = total + ventas[i]
        i += 1 
    return total

def calcular_porcentaje(venta, total):
    if total == 0:
        return 0
    porcentaje = venta * 100 / total
    return porcentaje

def calcular_promedio(ventas):
    if len(ventas) == 0:
        return 0
    total = calcular_total(ventas)
    promedio = total / len(ventas)
    return promedio

def buscar_mayor(ventas):
    if len(ventas) == 0:
        return 0 
    mayor = ventas[0]

    i = 1 

    while i < len(ventas):
        if ventas[i] > mayor:
            mayor = ventas [i]
        i += 1
    return mayor 

