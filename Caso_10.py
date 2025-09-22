#Caso 10
#Hotel
#Habitaciones y estado(0=libre/1=ocupada)

habitaciones=[]
estados=[]
opc=0

while opc!=8:
    print("\nMENÚ DE OPCIONES")
    print("1.Ingresar numeros de habitacion.")
    print("2.Ingresar estado de la habitacion.")
    print("3.Mostrar estado general.")
    print("4.Consultar estado de una habitacion.")
    print("5.Lista de habitaciones ocupadas/libres.")
    print("6.Agregar habitacion.")
    print("7.Cambiar estado de una habitacion.")
    print("8.Salir")

    opc=input("\nIngrese la opcion seleccionada: ")
    while not opc.isdigit():
        opc=input("\nDebe elegir una opcion del 1 al 8. Intente de nuevo: ")
        continue
    opc=int(opc) 
    match opc:
        case 1: #Ingresar nuemro de habitaciones
            cantidad=input("\nCantidad de habitaciones que desea ingresar: ")
            while not cantidad.isdigit():
                cantidad=input("\nCantidad incorrecta. Intente de nuevo: ")
                continue
            cantidad=int(cantidad)
            for i in range(cantidad):
                habitacion=input(f"\nIngresar numero de habitacion {i+1}:")
                while not habitacion.isdigit() or habitacion=="" or habitacion in habitaciones:
                    habitacion=input(f"\nHabitacion invalida o existente.Ingrese de nuevo la habitacion {i+1}: ")
                    continue
                habitaciones.append(habitacion)
                estados.append(0)
            
        case 2: #Ingresar estado de cada habitacion (0=libre/1=ocupada)
            if not habitaciones:
                print("\nNo hay habitaciones registradas.")
            else:
                for i in range(len(habitaciones)):
                    print("\nEstado de la habitacion:")
                    print("0.Libre")
                    print("1.Ocupada")

                    while True:
                        estado=input(f"Ingrese estado de la habitacion {habitaciones[i]}: ")
                        if estado in ["0","1"]:
                            break
                        else:
                            print("Opcion invalida.Ingrese nuevamente")

                    estado=int(estado)

                    if estado==0: #Libre
                        estados[i]="Libre"
                    elif estado==1: #Ocupada
                        estados[i]="Ocupada"
                    else:
                        print("Opcion invaida")
        
        case 3:
            if not habitaciones:
                print("\nNO hay habitaciones cargadas")
            else:
                print("\nListado de habitaciones con su disponibiladad")
                for i in range(len(habitaciones)):
                    print(f"Habitacion {habitaciones[i]} - {estados[i]}")
        
        case 4: #Consultar estado de una habitacion
            if not habitaciones:
                print("\nNO hay habitaciones cargadas")
            else:
                habitacion=input("\nIngrese numero de la habitacion a consultar: ")
                if habitacion in habitaciones:
                    indice=habitaciones.index(habitacion)
                    print(f"Habitacion: {habitaciones[indice]} - {estados[indice]}")
                else:
                    print("\nHabitacion no encontrada")
        
        case 5: #Listado de habitaciones libres/ocupada
            if not habitaciones:
                print("\nNO hay habitaciones cargadas")
            else:
                print("Ingrese que listado desea ver")
                print("0.Libres")
                print("1.Ocupadas")
                while True:
                        disponibiladad=input("Opcion 0 / 1: ")
                        if disponibiladad in ["0","1"]:
                            break
                        else:
                            print("Opcion invalida.Ingrese nuevamente")

                disponibiladad=int(disponibiladad)
                if disponibiladad==0: #LIbres
                    print("\nListado de Habitaciones Libres")
                    for i in range(len(habitaciones)):
                        if estados[i]=="Libre":
                            print(f"Habitacion {habitaciones[i]}")
                else:
                    print("\nListado de Habitaciones Ocupadas")
                    for i in range(len(habitaciones)):
                        if estados[i]=="Ocupada":
                            print(f"Habitacion {habitaciones[i]}")

        case 8:
            print("Hasta luego, gracias por utilizar nuestro sistema de reservas.")
            break

        case _:
            print("\nOpcion invalida")