def temperatura_ambiental(t):
    D = 7
    A = 9

    if t < 10:
        p = A*D+t
    else:
        p = A*D-t

    return p

########################

x = int(input("Ingrese la temperatura: "))
temperatura = temperatura_ambiental(x)
print("El resultado es: ",temperatura)
