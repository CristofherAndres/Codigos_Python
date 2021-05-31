i = 0
mayor = -99999999999999999
while i<3:
    num = int(input("Ingrese un número: ")) 
    if mayor < num:
        mayor = num

    i+=1

print("El mayor es:",mayor)