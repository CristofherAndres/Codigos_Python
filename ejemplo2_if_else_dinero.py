#Datos de entrada
costo = int(input("Ingrese el costo del producto: "))

#Proceso y salida
if costo <= 10000:
    print("Te recomiendo pagar con efectivo")
elif (costo > 10000 and costo < 30000):
    print("Te recomiendo pagar con debito")
else:
    print("Te recomiendo pagar con credito")