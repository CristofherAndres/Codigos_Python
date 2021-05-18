print("¡Bienvenido a nuestro categotizador de triangulos!")

lado1 = float(input("Ingrese el lado 1: "))
lado2 = float(input("Ingrese el lado 2: "))
lado3 = float(input("Ingrese el lado 3: "))

if lado1 > 0 and lado2 > 0 and lado3 > 0:
    if lado1 == lado2 and lado2 == lado3:
        print("Triangulo equilatero")
    elif lado1==lado2 or lado1==lado3 or lado2==lado3:
        print("Triangulo isosceles")
    else:
        print("Triangulo escaleno")
else:
    print("Datos ingresados no validos")