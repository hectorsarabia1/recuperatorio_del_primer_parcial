def numero_entero(dato):
    if len(dato):
        return False

    i = 0 

    while i < len(dato):
        caracter = dato[i]
        if caracter < 0 or caracter > 9:
            return False
        i += 1
    return True

def entero_positivo(texto):
    
    dato_valido = False
    numero = 0

    while dato_valido == False:
        dato = input(texto)

        if numero_entero(dato):
            numero = int(dato)
            if numero > 0:
                dato_valido = True
            else:
                print("El numero debe ser mayor que cero. ")
        else:
            print("Ingrese solamente numeros enteros. ")
    return numero

def opcion_menu():
    opcion_valida = False 
    opcion = -1

    while opcion_valida == False:
        dato = input("Seleccione una opcion (0-10): ")
        if numero_entero(dato):
            opcion = int(dato)
            if opcion >= 0 and opcion <= 10:
                opcion_valida = True
            else:
                print("La opcion debe estar entre 0 y 10.")
    return opcion


