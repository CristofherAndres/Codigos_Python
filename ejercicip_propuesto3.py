#datos de entrada
saldo = int(input("Ingresa el saldo: "))
costo = int(input("Ingresa el costo del pasaje: "))

#desarrollo
pasajes = saldo//costo
vuelto = saldo%costo



#Salida
print("La cantidad de viajes que le alcanza es:",pasajes)
print("El vuelto es:",vuelto, "y necesita",costo-vuelto,"para otro pasaje" )