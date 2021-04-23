#Importo la libreria matematica
import math

#Entrada de datos
numero = int(input("Ingrese un numero mayor que cero..."))

#calculo de la raiz
raiz = math.sqrt(numero)

#redondear
raiz = round(raiz,20)

#salida
print("La raiz cuadrada es...",raiz)
