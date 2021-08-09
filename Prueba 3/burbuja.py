def validar_order(datos):
    largo = len(datos)
    contador=0
    for i in range(largo-1):
        if datos[i]<=datos[i+1]:
            contador+=1    
    if contador==largo-1:
        return False
    return True
            
###############################


cant = int(input("¿Cuantos datos quiere ingresar?:  "))

datos = []
for i in range(cant):
    dato = int(input("Ingrese el dato "+str(i+1)+":  "))
    datos.append(dato)

print(datos)

largo = len(datos)

valida=True

while valida:
    for i in range(largo-1):
        if datos[i] > datos[i+1]:
            aux=datos[i]
            datos[i] = datos[i+1]
            datos[i+1]=aux
    valida=validar_order(datos)


print(datos)