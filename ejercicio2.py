#Datos de entrada
base = float(input("Ingrese base: "))
altura = float(input("Ingrese altura: "))

#Proceso
perimetro = round(2*base*altura,1)

area = base*altura
area = round(area,1)

#salida
print("El área es: ",area)
print("El perimetro es: ",perimetro)
