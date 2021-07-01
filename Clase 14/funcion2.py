def calcular_vuelto(costo, pago):
    vuelto = pago-costo
    return vuelto
 

#########

x = int(input("Ingrese el total a pagar: "))
y = int(input("Dinero del pago: "))

print("El vuelto es",calcular_vuelto(x,y))