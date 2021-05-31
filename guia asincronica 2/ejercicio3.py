import math as m
segundos = int(input("Ingrese la cantidad de segundos: "))

if segundos>=0:
    
    if segundos%60 == 0:
        print("Tiene",m.trunc(segundos/60) ,"minutos")
        print("No faltan segundos para minutos exactos")
    else:
        print("Tiene",m.trunc(segundos/60) ,"minutos y",segundos%60,"segundos")
        print("Necesita",60-segundos%60,"segundos para completar minutos exactos")
    
else:
    print("Ingrese datos correctamente")