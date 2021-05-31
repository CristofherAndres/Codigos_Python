#entrada de los datos

str = "El pollo dice guau guau cuando esta enojado"
print(str)
corregir = input("¿Que deberia decir? En lugar de pollo... ")
corregir = corregir.strip()
corregir = corregir.lower()

while corregir != 'perro':
    print(str.replace("pollo", corregir))
    corregir = input("¿Que deberia decir? En lugar de pollo... ")
    corregir = corregir.strip()
    corregir = corregir.lower()

print(str.replace("pollo", corregir))