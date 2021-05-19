if dia==31:
    if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
        print("Fecha valida")
elif dia == 30:
    if mes==4 or mes==6 or mes==9 or mes==11:
        print("Fecha valida")
elif dia == 29 and anho_bisiesto==True:
        print("Fecha valida")
elif dia == 28 and anho_bisiesto==False:
        print("Fecha valida")
else:
    print("Fecha invalida")