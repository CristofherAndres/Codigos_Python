def sumar_digitos(num):
    numTxt = str(num)
    largo = len(numTxt)
    suma= 0

    for i in range(largo):
        if numTxt[i]!='-':
            suma= suma + int(numTxt[i])

    return suma

def suma_lista(numeros):
    suma=0
    for i in numeros:
        suma = suma + i
    
    return suma

#####################
numeros = []
num = int(input("Ingrese un número: "))

if num!=0:
        print("La suma de sus digitos es:",sumar_digitos(num))
        numeros.append(num)
else:
    print("Gracias por usar el programa")

while num != 0:
    num = int(input("Ingrese un número: "))
    if num!=0:
        print("La suma de sus digitos es:",sumar_digitos(num))
        numeros.append(num)
    else:
        break
    

print("La suma de todos los números es:",suma_lista(numeros))
