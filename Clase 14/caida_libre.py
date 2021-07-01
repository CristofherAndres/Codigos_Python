def caidaLibre(t):
    h = 1/2*9.8*t**2
    return h

tiempo = int(input("Ingresa el tiempo: "))
altura = caidaLibre(tiempo)
print("La altura es:",altura)