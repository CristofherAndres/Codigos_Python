print("Bienvenido al triangulo de asteriscos")

ancho = int(input("Ingresa un ancho para tu triangulo: "))


i=0
while i<=ancho:
    j=0
    while j<i:
        print("*",end="")
        j+=1
    print()
    i+=1

i=9
while i>=0:
    j=0
    while j<i:
        print("*",end="")
        j+=1
    print()
    i-=1