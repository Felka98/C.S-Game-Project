inp=0
def sumatoria(a,b):
    suma=0
    while a<=b:
        suma+=a
        a+=1
    return suma
def Kg_LBS(kilos):
    return kilos*2.2
def lbs_Kg(libras):
    return libras/2.2
def dividir(a,b):
    return a/b
print("Bienvenido")
print("Escoja una opcion:")
print("1.Ingresar dos numeros")
print("2.Calcular sumatoria")
print("3.Convertir de kg a lbs")
print("4.Convertir de lbs a kg")
print("5.Dividir los numeros")
print("6.Salir")
opcion=int(input("Opcion: "))
while inp!=6:
    num1=int(input("Mandese un numero: "))
    if inp==2:
        pass
    elif inp==3:
        pass
    elif inp==4:
       pass
    elif inp==5:
        pass
if inp==6:
    print("Buen dia!")