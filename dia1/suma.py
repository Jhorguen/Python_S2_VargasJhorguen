print("Hola bienvenido a mi calculadora")

#PIDO Y CONVIERTO EN ENTERO CADA DATO INGRESADO#
num1 = int(input("Ingresa el primer numero a sumar"))
num2 = int(input("Ingresa el segundo numero a sumar"))

#SUMO LOS DATOS INGRESADO Y CREO UNA VARIABLE PARA ALLI GUARDAR EL REULTADO DE DICHA SUMA#
resultado = num1 + num2
print(resultado)

#IMPRIMO LA SUMNA DE LOS DOS NUMERO CONCATENANDO LA VARIABLE RESULTADO CONVIRTIENDOLA EN STRING PARA PORDER CONCATENARLA#
print("El resultado de tu suma es: "+ str(resultado))
