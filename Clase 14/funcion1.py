#función para calcular el area de un triangulo
# Def <- Indica que es una función

def AreaTriangulo(base, altura):
    area = (base*altura)/2
    return area

##########################################

baseEntrada = int(input("Ingresa la base: "))
alturaEntrada = int(input("Ingresa la altura: "))

area = AreaTriangulo(baseEntrada,alturaEntrada)

print(area)