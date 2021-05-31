import math as m

cantHoras = int(input("Cantidad de horas semanales asistidas:  "))

if cantHoras >= 0:
    
    minutos = cantHoras*45

    horas = m.trunc(minutos/60)
    minutos = minutos%60

    print("La cantidad de horas cronologicas es:",horas,end=" ")
    if minutos>0:
        print("y",minutos,"minutos")
    else:
        print()

    
else:
    print("Debe ingresar una cantidad positiva")