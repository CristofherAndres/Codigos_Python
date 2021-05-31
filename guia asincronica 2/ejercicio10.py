horas = int(input("Ingrese las horas de trabajo: "))
pagoxhora = int(input("Ingrese el valor de la hora: "))

if horas > 45:
    sueldo = horas*pagoxhora*1.5
else:
    sueldo = horas*pagoxhora

print("El sueldo es",sueldo)