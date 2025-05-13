divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

print("Que divisa desea ver su simbolo? 1.Euro 2.Dollar 3.Yen")
eleccionDivisa= int(input())

if(eleccionDivisa == 1):
   print("El simbolo es: ",divisas['Euro'])

elif(eleccionDivisa==2):
   print("El simbolo es: ",divisas['Dollar'])

elif(eleccionDivisa==3):
   print("El simbolo es: ", divisas['Yen'])

else:
   print("Escoge una opcio correcta.")
