user={
    "nombre":"",
    "edad":"",
    "direccion":"",
    "numero": ""
}



print("Bienvenido")

print("Cual es tu nombre")
name=input()
user["nombre"]=name

print("Cual es tu edad")
age=int(input())
user["edad"]=age

print("Cual es tu direccion")
direction=input()
user["direccion"]=direction

print("Cual es tu numero de telefono")
phoneNumber=int(input())
user["numero"]=phoneNumber


print("------------------------------")
print(user["nombre"], " tiene ",user["edad"]," años, vive en ",user["direccion"]," y su numero de telefono es ", user["numero"])
print("------------------------------")
