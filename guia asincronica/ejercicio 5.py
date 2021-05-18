print("Bienvenido a nuestro validador de fechas")

dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
anho = int(input("Ingrese el año: "))

anho_bisiesto = False

#Calcular si es bisiesto

if anho % 4 == 0 and not anho % 100 == 0:
    anho_bisiesto = True
elif anho % 100 == 0 and anho % 400 == 0:
    anho_bisiesto = True
    

if dia==31:
    if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
        print("Fecha valida")
    else:
        print("Fecha invalida")
elif dia == 30:
    if mes==4 or mes==6 or mes==9 or mes==11:
        print("Fecha valida")
    else:
        print("Fecha invalida")
elif dia == 29 and anho_bisiesto==True:
        print("Fecha valida")
elif dia == 28 and anho_bisiesto==False:
        print("Fecha valida")
else:
    print("Fecha invalida")
