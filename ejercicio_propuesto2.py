#entrada

agua = int(input("Ingrese el valor del agua: "))
luz = int(input("Ingrese el valor del luz: "))
internet = int(input("Ingrese el valor del internet: "))
gas = int(input("Ingrese el valor del gas: "))
netflix = int(input("Ingrese el valor del netflix: "))
cable = int(input("Ingrese el valor del cable: "))


#Proceso

total = agua + luz + internet + gas + netflix + cable

#Salida
print("El total de los gastos es: "+str(total))
