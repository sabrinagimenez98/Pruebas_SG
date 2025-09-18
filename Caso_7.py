print("\n Sistema de gestion de asistencias de los Estudiantes")
estudiantes=[]
asistencias=[]

import random

opcion=0

while opcion!=9:
    
    print("\n Menu de opciones")
    print("1.Ingresar estudiantes")
    print("2.Ingrsar asistencias")
    print("3.Mostrar listado de estudiantes y asistencias")
    print("4.Consultar asistencia de un alumno")
    print("5.Listado de estudiantes con 0 asistencias")
    print("6.Agregar nuevo estudiante")
    print("7.Estudiantes con 0 asistencias")
    print("8.Ingresar asistencia")
    print("9.Salir del programa")
    opcion=int(input("\n Ingrese una opcion: "))

    if opcion==1:
        estudiantes.clear()
        asistencias.clear()
        cantidad= int(input("\n Cantidad de alumnos a ingresar: "))
        for i in range(cantidad):
            estudiante=input(f"\nIngrese nombre del Estudiante {i+1}: ").title()
            while estudiante == "" or estudiante in estudiantes :
                estudiante=input("\n Estudiante duplicado o invalido. Ingrese nuevamente: ")
            asistencia=0
            estudiantes.append(estudiante)
            asistencias.append(asistencia)
            
    if opcion==2:
        for i in range(cantidad):
            asistencias[i]=random.randint(1,10)
        print(asistencias)

    if opcion==3:
            print("\n Listado de estudiantes con sus asistencias")
            for i in range(len(estudiantes)):
                 print(f"Estudiante {i+1}: {estudiantes[i]} - Asistencias: {asistencias[i]}")

    if opcion==4:
         estudiante=input("\n Ingrese estudiante que quiere consultar: ").title()
         if estudiante in estudiantes:
              indice=estudiantes.index(estudiante)
              print(f"\n Estudiante: {estudiante} - Asistencia: {asistencias[indice]}")
         
    if opcion==5:
        if 0 in asistencias:
            for i in range(len(estudiantes)):
                if asistencias[i]==0:
                    print(estudiantes[i])
        else:
             print("\n No hay estudiantes con 0 asistecias")
         
print("\n Gracias por usar el sistema de Asistencias")