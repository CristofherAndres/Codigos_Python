
diccionario = {
    'Nombre' : 'Cristofher',
    'Edad' : 28,
    'Ramos' : ['Programación' , 'Bases de datos', 'Sistemas de información']
}



Texto_salida = "Hola, mi nombre es XXXXX, tengo YY años y dicto las siguientes asignaturas: "

Texto_salida=Texto_salida.replace("XXXXX",diccionario['Nombre'])
Texto_salida=Texto_salida.replace("YY",str(diccionario['Edad']))


for i in diccionario['Ramos']:
    Texto_salida += i + ", "

print(Texto_salida)