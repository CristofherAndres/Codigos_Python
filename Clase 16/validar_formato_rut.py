

rut=input("Ingrese su rut: ")

#eliminamos espacios blancos delante y atras del texto
rut_formateado = rut.strip()

#Eliminar puntos
#rut_formateado = rut.replace('.','')

if rut_formateado[-1].upper()=='K':
    print("finaliza en K")
elif rut_formateado[-1].isdigit():
    print("Finaliza en Número")
else:
    print("El rut es erroneo")

nuevo_rut = ''

for i in rut_formateado:
    if i.isdigit():
        nuevo_rut=nuevo_rut+i
    elif i.upper() == 'K':
        nuevo_rut=nuevo_rut+i

print(nuevo_rut)



print(rut_formateado)
