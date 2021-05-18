print("Bienvenido al programa de mayor y menor")

num1 = float(input("Ingrese el número 1: "))
num2 = float(input("Ingrese el número 2: "))
num3 = float(input("Ingrese el número 3: "))

if (num1>num2 and num1>num3):
    print("El numero mayor es",num1)
elif (num2>num1 and num2>num3):
    print("El numero mayor es",num2)
elif (num3>num1 and num3>num2):
    print("El numero mayor es",num3)
elif (num1==num2 and num1>num3):
    print("El numero mayor es",num1)
elif (num1==num3 and num1>num2):
    print("El numero mayor es",num1)
elif (num2==num3 and num2>num1):
    print("El numero mayor es",num2)
else:
    print("El numero mayor es",num1)

if (num1<num2 and num1<num3):
    print("El numero menor es",num1)
elif (num2<num1 and num2<num3):
    print("El numero menor es",num2)
elif (num3<num1 and num3<num2):
    print("El numero menor es",num3)
elif (num1==num2 and num1<num3):
    print("El numero menor es",num1)
elif (num1==num3 and num1<num2):
    print("El numero menor es",num1)
elif (num2==num3 and num2<num1):
    print("El numero menor es",num2)
else:
    print("El numero menor es",num1)