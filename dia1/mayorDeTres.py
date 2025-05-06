#solicito la entrada de los 3 numeros a evaluar#

print("Hola por favor ingresa los numero a evaluar")
num1 = int(input("Ingresa el primer numero"))
num2 = int(input("Ingresa el segundo numero"))
num3 = int(input("Ingresa el tercer numero"))

if(num1 > num2):
    mayor1 = num1
else:
    mayor1 = num2

if(mayor1 > num3):
    mayorFinal = mayor1
else:
    mayorFinal = num3
    
print("El numero mayor es: "+str(mayorFinal))