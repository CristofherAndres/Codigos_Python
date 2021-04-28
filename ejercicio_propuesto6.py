#Datos de entrada
dinero = int(input("Ingrese el dinero: "))

b10 = dinero//10000
dinero = dinero%10000
print("Billetes de 10.000:",b10)

b5 = dinero//5000
dinero = dinero%5000
print("Billetes de 5.000:",b5)

b1 = dinero//1000
dinero = dinero%1000
print("Billetes de 1.000:",b1)

m500 = dinero//500
dinero = dinero%500
print("Moneda de 500:",m500)

m100 = dinero//100
dinero = dinero%100
print("Moneda de 100:",m100)

m50 = dinero//50
dinero = dinero%50
print("Moneda de 50:",m50)

m10 = dinero//10
dinero = dinero%10
print("Moneda de 10:",m10)

m5 = dinero//5
dinero = dinero%5
print("Moneda de 5:",m5)

m1 = dinero
print("Moneda de 1:",m1)