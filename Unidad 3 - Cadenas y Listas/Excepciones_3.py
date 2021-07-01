while True:
# Se entra en un bucle infinito
# Se pide introducir un número
    numero = input("Introduzca un número entre 1 y 10: ")
    try:
        numero = int(numero)
    except:
        pass
    else:
    # Realizar la comparación
        if 1 <= numero <= 10:
        # Tenemos lo que queremos, de modo que salimos del bucle
            break
        
print("Estamos seguros de que", numero, "es un número y está comprendido entre 1 y 10 incluidos")