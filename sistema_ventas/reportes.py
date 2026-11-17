from sistema_ventas.operaciones import (
    calcular_total,
    calcular_porcentaje,
    calcular_promedio,
    buscar_mayor
)

def mostrar_ventas(nombres, ventas):

    total = calcular_total(ventas)
    print("--- Ventas por Region ---")

    i = 0

    while i < len(ventas):
        porcentaje = calcular_porcentaje(ventas[i], total)
        print("Region: ", i + 1, nombres[i])
        print("Cantidad de ventas:", ventas[i])
        print("Porcentaje:", porcentaje,"%")

        i += 1
    print("Total de productos vendidos: ", total)

def regiones_porcentaje(nombres, ventas, limite):
    total = calcular_total(ventas)
    cantidad_encontrada = 0
    ventas_acumuladas = 0 

    print("--- Regiones con menos del", limite, "%---")
    i = 0 
    while i < len(ventas):
        porcentaje = calcular_porcentaje(ventas[i], total)
        if porcentaje < limite:
            cantidad_encontrada += 1 
            ventas_acumuladas += ventas[i]

            print("Region: ", nombres[i])
            print("Cantidad de ventas: ", ventas[i])
            print("Porcentajes: ", porcentaje, "%")

        i += 1
    if cantidad_encontrada == 0:
        print("No se encontraron regiones.")
    else:
        porcentaje_acumulado = calcular_porcentaje(
            ventas_acumuladas, total
        )
        print("Porcentaje acumulado: ", porcentaje_acumulado, "%")

def regiones_por_cantidad(nombres, ventas, limite):
    cantidad_encontrada = 0
    ventas_acumuladas = 0
    total = calcular_total(ventas)

    print("--- Regiones con mas de ", limite, "ventas ---")

    i = 0

    while i < len(ventas):
        if ventas[i]>limite:
            cantidad_encontrada += 1
            ventas_acumuladas += ventas[i]

            porcentaje = calcular_porcentaje(vemtas[i], total)
            print("Region: ", nombres[i])
            print("Cantidad de ventas: ", ventas[i])
            print("Porcentajes: ", porcentaje, "%")

        i += 1

    if cantidad_encontrada == 0:
        