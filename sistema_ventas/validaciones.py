def numero_entero(dato):
    if len(dato):
        return False

    i = 0 

    while i < len(dato):
        caracter = dato[i]
        if caracter < 0 or caracter > 9: