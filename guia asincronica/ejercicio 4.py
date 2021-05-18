print("Bienvenido al medidor de tornillos")

tamano_tornillo = float(input("Ingrese el tamaño del tornillo a medir: "))

if tamano_tornillo >= 1 and tamano_tornillo<3:
    print("Pequeño")
elif tamano_tornillo >= 3 and tamano_tornillo<5:
    print("Mediano")
elif tamano_tornillo >= 5 and tamano_tornillo<6.5:
    print("Grande")
elif tamano_tornillo >= 6.5 and tamano_tornillo<8.5:
    print("Muy grande")
else:
    print("Medida no valida")