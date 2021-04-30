#Datos de entrada
semaforo = input("Ingrese el color del semaforo: ")

#La entrada se pasa a mayuscula
semaforo = semaforo.upper()

#Proceso y salida
if semaforo == "VERDE":
    print("Puedes cruzar la calle")
elif (semaforo == "AMARILLO"):
    print("Puedes cruzar la calle, pero apurate")
elif (semaforo == "ROJO"):
    print("DETENTE")
else:
    print("Debes poner un color correcto")
