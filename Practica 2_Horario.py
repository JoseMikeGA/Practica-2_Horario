#Control inventario de una empacadora
import numpy as np
contenido=np.zeros((3,1))
class inven():
    def __init__(self):
        pass
    def meter(self,cantidad):
        nombre=int(input("Elije que objeto deseas agregar:\n\t1. Caja chica\n\t2. Caja mediana\n\t3. Caja grande\n"))
        if(nombre==1):
            contenido[0]=contenido[0]+x
        if(nombre==2):
            contenido[1]=contenido[1]+x
        if(nombre==3):
            contenido[2]=contenido[2]+x
        return(contenido)
    def sacar(self,cantidad):
        nombre=int(input("Elije que objeto deseas retirar:\n\t1. Caja chica\n\t2. Caja mediana\n\t3. Caja grande\n"))
        if(nombre==1):
            if(x>contenido[0]):
                print("La cantidad de cajas a retirar excede el inventario disponible")
            elif(contenido[0]>x):
                contenido[0]=contenido[0]-x
        if(nombre==2):
            if(x>contenido[1]):
                print("La cantidad de cajas a retirar excede el inventario disponible")
            elif(contenido[1]>x):
                contenido[1]=contenido[1]-x
        if(nombre==3):
            if(x>contenido[2]):
                print("La cantidad de cajas a retirar excede el inventario disponible")
            elif(contenido[2]>x):
                contenido[2]=contenido[2]-x
        return(contenido)
    def consultar(self):
        print("Tenemos en existencia "+str(contenido[0])+" cajas chicas\n"+"Ademas de "+str(contenido[1])+" cajas medianas\n"+"Y por último "+str(contenido[2])+" cajas grandes\n")

objeto1=inven()
while (True):
    a=0
    opcion=int(input("Buen día, que acción desea realizar el dia de hoy:\n\t1. Agregar cajas al inventario\n\t2. Retirar cajas del inventario\n\t3. Consultar el numero de cajas en elinventario\n"))
    if(opcion==1):
        x=int(input("Cuantas cajas desea ingresar al inventario: "))
        a=objeto1.meter(x)
    elif(opcion==2):
        x=int(input("Cuanta cajas desea retirar del inventario: "))
        a=objeto1.sacar(x)
    elif(opcion==3):
        a=objeto1.consultar()
    else:
        print("Opcion no valida")
    salir=input("¿Desea realizar alguna otra operación?\n\ts=si\n\tn=no\n")
    if(salir=="n"):
        print("Nos vemos pronto, que tenga un excelente día")
        break