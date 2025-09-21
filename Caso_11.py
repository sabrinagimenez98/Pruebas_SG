#PROGRAMA PARA TALLER
#Ordenes de reparacion y tiempos estimados

ordenes=[]
ordenes_numericas=[]
tiempos=[]
opc=0

while opc!=8:
    print("\nMENU DE OPCIONES")
    print("1.Ingresar ordenes.")
    print("2.Ingresar horas estimadas por orden.")
    print("3.Mostrar agenda del taller.")
    print("4.Consultar tiempo estimado por orden.")
    print("5.Listado de ordenes pendientes de diagnostico.")
    print("6.Agregar nueva orden.")
    print("7.Actualizar ordenes (Adelanto/Retraso).")
    print("8.Salir")

    opc=input("\nIngrese opcion:")
    while not opc.isdigit():
        opc=input("\nOpcion invalida.Ingrese una opcion del 1 al 8: ")
        continue
    opc=int(opc)
    match opc:
        case 1: #Ingresar ordenes
            ordenes.clear() #Limpia la lista de ordenes cada vez que se utiliza la opcion 1
            cantidad=input("\nCantidad de ordenes que desea cargar: ")

            while not cantidad.isdigit():
                cantidad=input("\nCantidad invalida.Ingrese un numero: ")
                continue
            cantidad=int(cantidad)

            for i in range(cantidad):
                orden_numerica=input(f"\nIngrese el numero de orden {i+1}: ")

                while not orden_numerica.isdigit():
                    orden_numerica=input("\nNumero invalida.Ingrese una opcion del 0 al 100: ")
                    continue
                
                while orden_numerica in ordenes_numericas:
                    orden_numerica=input("Orden duplicada.Intente de nuevo : ")
                    continue
                
                ordenes_numericas.append(orden_numerica)
                orden_numerica=orden_numerica.zfill(3)
                orden="ORD-"+orden_numerica
                ordenes.append(orden)
                tiempos.append(0)
        case 2: #Ingresa diagnostico
            if len(ordenes)==0:
                print("\nNo hay ordenes cargadas")
            else:
                for i in range(len(ordenes)):
                    tiempo=input(f"\nIngrese el tiempo estimado de {ordenes[i]}: ")
                    while not tiempo.isdigit():
                        print("Recomendamos utilizar numeros enteros")
                        tiempo=input("\nOpcion invalida.Ingrese nuevamente el tiempo estimado: ")
                        continue
                    tiempos[i]=int(tiempo)
        case 3:
            if len(ordenes)==0:
                print("\nNo hay ordenes cargadas")
            else:
                print("\nListado de ordenes con sus tiempos estimados")
                for i in range(len(ordenes)):
                    print(f"{ordenes[i]} - Tiempo estimado: {tiempos[i]} horas")
        case 4: #Consultar pot una orden
            if len(ordenes)==0:
                print("\nNo hay ordenes cargadas")
            else:
                orden_numerica=input(f"\nIngrese solo el numero de orden: ")

                while not orden_numerica.isdigit():
                    orden_numerica=input("\nNumero invalida.Ingrese una opcion del 0 al 100: ")
                    continue
                orden_numerica=orden_numerica.zfill(3)
                orden="ORD-"+orden_numerica
                if orden in ordenes:
                    indi=ordenes.index(orden)
                    print(f"\n{ordenes[indi]} - Tiempo estimado: {tiempos[indi]} horas")
                else:
                    print("\nNo se ha encontrado la orden")
        case 5: #Listado de Ordenes pendientes de diagnostico(Tiempo=0)
            if not ordenes:
                print("\nNo hay ordenes cargadas")
            elif 0 in tiempos:
                print("\nListado de Ordenes pendientes")
                for i in range(len(ordenes)):
                    if tiempos[i]==0:
                        print(f"{ordenes[i]}")
            else:
                print("\nNo hay ordenes pendientes")
        case 6: #Agregar nueva orden
            orden_numerica=input("\nIngrese el nuevo numero de orden que desea cargar")

            while not orden_numerica.isdigit():
                    orden_numerica=input("\nNumero invalida.Ingrese una opcion del 0 al 100: ")
                    continue
                
            while orden_numerica in ordenes_numericas:
                    orden_numerica=input("Orden duplicada.Intente de nuevo : ")
                    continue
                
            ordenes_numericas.append(orden_numerica)
            orden_numerica=orden_numerica.zfill(3)
            orden="ORD-"+orden_numerica
            ordenes.append(orden)
            tiempo=input(f"\nIngrese el tiempo estimado de {orden}: ")
            while not tiempo.isdigit():
                print("Recomendamos utilizar numeros enteros")
                tiempo=input("\nOpcion invalida.Ingrese nuevamente el tiempo estimado: ")
                continue
            tiempos.append(int(tiempo))
        case 7: #Actualizar ordenes
            if not ordenes:
                print("No hay ordenes cargadas")
            else:
                print("\nActualizacion de notas")
                print("1.Adelanto")
                print("2.Retrazo")
                opcion=int(input("Selecciona una opcion (1/2): "))
                orden_numerica=input(f"\nIngrese el numero de orden: ")
                while not orden_numerica.isdigit():
                    orden_numerica=input("\nNumero invalida.Ingrese una opcion del 0 al 100: ")
                    continue
                if orden_numerica in ordenes_numericas:
                    indice=ordenes_numericas.index(orden_numerica)
                    print(f"{ordenes[indice]} - {tiempos[indice]} horas")
                    cantidad=input("Cantidad de horas a adelantar/atrasar:")
                    while not cantidad.isdigit():
                        cantidad=input("\nNumero invalido.Ingrese una nueva cantidad: ")
                        continue
                    cantidad=int(cantidad)
                    if opcion==1:
                        if cantidad<=0:
                            print("No hay cantidad a actualizar")
                        elif cantidad>tiempos[indice]:
                            print("No hay tiempo suficiente para adelantar")
                        else:
                            tiempos[indice]-=cantidad
                            print(f"\n {ordenes[indice]} - Nuevo tiempo: {tiempos[indice]} horas")
                    elif opcion==2:
                        if cantidad<=0:
                            print("No hay cantidad a actualizar")
                        else:
                            tiempos[indice]+=cantidad
                            print(f"\n {ordenes[indice]} - Nuevo tiempo: {tiempos[indice]} horas")
                    else:
                        print("\nOpcion invalida.")
                else:
                    print("\nNo se ha encontrada la orden")
        case 8: #Salir del menu
            print("\nHasta luego. Gracias por utilizar nuestro programa")
            break
        case _:
            print("\nOpcion invalida.")