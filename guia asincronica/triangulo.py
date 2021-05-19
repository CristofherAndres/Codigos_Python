print("Bienvenido al triangulo de asteriscos")

ancho = int(input("Ingresa un ancho para tu triangulo: "))

for i in range(1,ancho+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
for i in range(ancho-1,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print()