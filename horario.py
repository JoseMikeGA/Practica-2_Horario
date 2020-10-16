#Horario 

import numpy as np

class day():
    def __init__(self, dia, actividad, hora):
            self.dia=dia
            self.actividad=actividad
            self.hora=hora

    def agregar(self):

        if(self.actividad=="No tiene ninguna actividad"):
            a=input("¿Que actividad desea agregar? ")
            self.actividad=a
            h=input("¿En que horario desea agregar su actividad? ")
            self.hora=h
        else:
            print("Lo siento ya tenemos una actividad agendada :( ")

    def consultar(self):
            if(self.dia=="Sabado" or self.dia=="Domingo"):
                print(self.dia,": Dia inhabil")
            else:
                print(self.dia, ": ",self.actividad, "a las ", self.hora)        

lunes=day("Lunes","No tiene ninguna actividad","--")
martes=day("Martes","No tiene ninguna actividad","--")
miercoles=day("Miercoles","No tiene ninguna actividad","--")
jueves=day("Jueves","No tiene ninguna actividad","--")
viernes=day("Viernes","No tiene ninguna actividad","--")
sabado=day("Sabado","No tiene ninguna actividad","--")
domingo=day("Domingo","No tiene ninguna actividad","--")

while (True):
    l=""
    m=""
    mi=""
    j=""
    v=""
    s=""
    d=""
    opcion=int(input("Buen dia, que le gustaria hacer?:\n\t1. Agendar actividad\n\t2. Consultar actividades\n"))
    if(opcion==1):
        opcion=int(input("¿En que día desea agendar su actividad?:\n\t1. Lunes\n\t2. Martes\n\t3. Miercoles\n\t4. Jueves\n\t5. Viernes\n\t6. Sabado\n\t7. Domingo\n"))
        if(opcion==1):
                l=lunes.agregar()
        elif(opcion==2):
                m=martes.agregar()
        elif(opcion==3):
                mi=miercoles.agregar()
        elif(opcion==4):
                j=jueves.agregar()
        elif(opcion==5):
                v=viernes.agregar()
        elif(opcion==6 or opcion==7):
                print("Lo siento, este día es inhabil")
        else:
                print("Opcion no admitida")

    elif(opcion==2):
        print("Las actividades de la semana son:")
        l=lunes.consultar()
        m=martes.consultar()
        mi=miercoles.consultar()
        j=jueves.consultar()
        v=viernes.consultar()
        s=sabado.consultar()
        d=domingo.consultar()
    else:
        print("Opcion no valida")
    
    salir=input("¿Desea hacer otra operacion?\n\ts=si\n\tn=no\n")
    if(salir=="n"):
        print("Hasta luego")
        break