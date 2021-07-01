from funciones import *

costo = int(input("Ingrese el total a pagar: "))
pago = int(input("Dinero del pago: "))

print("El vuelto es",calcular_vuelto(costo,pago))

print("El area es",AreaTriangulo(costo,pago))