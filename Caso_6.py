#PROGRAMA PARA EVENTOS
eventos=[]
entradas=[]
opc=0

while opc!=8:
    print("\nMenu de opciones para Eventos y entradas")
    print("1.Ingrear shows.")
    print("2.Ingresar entradas por show.")
    print("3.Mostrar Shows-Entradas.")
    print("4.Consultar entradas de un show.")
    print("5.Listado de show agostados.")
    print("6.Agregar nuevo show.")
    print("7.Actualizar entradas(venta/devolucion).")
    print("8.Salir del programa.")

    opc=input("\nIngrese una opcion: ")
    while not opc.isdigit():
        opc=input("\nOpcion invalida. Ingrese un número de 1 al 8: ")
        continue
    opc=int(opc)
    match opc:
        case 1: #Ingresar eventos
            eventos.clear() #Se limpia cada vez que se selecciona esta opcion
            cant=input("\nCantidad de eventos que desea cargar: ")
            while not cant.isdigit():
                cant=input("\nOpcion invalida. Intente de nuevo: ")
                continue
            cant=int(cant)
            for i in range(cant):
                evento=input(f"\nIngresar evento {i+1}: ").title()
                while evento=="" or evento in eventos:
                    evento=input(f"\nEvento vacio o duplicado. Ingrese nuevamente el evento {i+1}: ")
                    continue
                eventos.append(evento)
                entradas.append(0)
        case 2: #Ingresar entradas por evento
                if not eventos:
                    print("\nPrimero debe ingresar Eventos (Opcion 1).")
                else:
                    for i in range(cant):
                        entrada=input(f"\nIngrese la cantidad de entradas de {eventos[i]}: ")
                        while not entrada.isdigit():
                            entrada=input(f"\nCantidad de entradas invalida. Cantidad de entradas de {eventos[i]}: ")
                            continue
                        entradas[i]=int(entrada)
        case 3: #Mostrar listado de Eventos - Entradas
            if not eventos:
                print("\nPrimero debe ingresar Eventos (Opcion 1).")
            else:
                print("\nListado de Eventos y Entradas")
                for i in range(len(eventos)):
                    print(f"{eventos[i]} - Entradas: {entradas[i]}")
        case 4: #Buscar un evento
            if not eventos:
                print("\nPrimero debe ingresar Eventos (Opcion 1).")
            else:
                evento=input("Evento por el cual desea consultar: ")
                if evento in eventos:
                    indice=eventos.index(evento)
                    print(f"{eventos[indice]} - Entradas: {entradas[indice]}")
                else:
                    print("Evento no encontrado")
        case 5: #Listado de eventos agotados
            if not eventos:
                print("\nPrimero debe ingresar Eventos (Opcion 1).")
            elif 0 in entradas:
                print("Listado de Show Agostados")
                for i in range(len(eventos)):
                    if entradas[i]==0:
                        print(f"{eventos[i]}")
            else:
                print("No hay Shows Agotados")
        case 6: #Agregar nuevo show
            cant=input("\nCantidad de eventos nuevos que desea cargar: ")
            while not cant.isdigit():
                cant=input("\nOpcion invalida. Intente de nuevo: ")
                continue
            cant=int(cant)
            for i in range(cant):
                evento=input(f"\nIngresar evento nuevo {i+1}: ").title()
                while evento=="" or evento in eventos:
                    evento=input(f"\nEvento vacio o duplicado. Ingrese nuevamente el evento {i+1}: ").title()
                    continue
                eventos.append(evento)

                entrada=input(f"\nIngrese la cantidad de entradas de {evento}: ")
                while not entrada.isdigit():
                    entrada=input(f"\nCantidad de entradas invalida. Cantidad de entradas de {evento}: ")
                    continue
                entradas.append(entrada)
        case 7: #7.Actualizar entradas(venta/devolucion)
            if not eventos:
                print("\nNoy eventos para actualizar.")
            else:
                print("\nAccion que desea realizar:")
                print("1.Venta de entradas.")
                print("2.Devolucion de entradas.")
                accion=int(input("Opcion elegida (1/2): "))

                if accion==1:
                    print("\nSistema de Venta de entradas")
                    evento=input("\nEvento que desea vender: ").title()
                    if evento in eventos:
                        cantidad=input(f"\nCantidad de entradas de {evento} que desea vender: ")
                        while not cantidad.isdigit():
                            cantidad=input("\nDebe ingresar un numero entero. Intente de nuevo: ")
                            continue
                        cantidad=int(cantidad)
                        indice=eventos.index(evento)

                        while cantidad>entradas[indice]:
                            cantidad=int(input("\nCantidad de entradas insuficientes para la venta. Intente de nuevo: "))
                            continue

                        while cantidad==0:
                            cantidad=int(input("\nDebe vender almenos 1 entrada. Intente de nuevo: "))
                            continue

                        entradas[indice] -= cantidad
                        print(f"\nEntradas sobrantes de {eventos[indice]}: {entradas[indice]}")
                    else:
                        print("Evento no disponible para la venta.")
                elif accion==2:
                    print("\nSistema de Devolucion de entradas")
                    evento=input("\nEvento que desea devolver: ").title()
                    if evento in eventos:
                        cantidad=input(f"\nCantidad de entradas de {evento} que desea devolver: ")
                        while not cantidad.isdigit():
                            cantidad=input("\nDebe ingresar un numero entero. Intente de nuevo: ")
                            continue
                        cantidad=int(cantidad)
                        indice=eventos.index(evento)

                        while cantidad==0:
                            cantidad=int(input("\nDebe vender almenos 1 entrada. Intente de nuevo: "))
                            continue

                        entradas[indice] += cantidad
                        print(f"\nEntradas totales de {eventos[indice]}: {entradas[indice]}")
                    else:
                        print("Evento no disponible para la venta.")
                else:
                    print("Opcion invalida")

        case 8: #Salir del programa
            print("Gracias por usar el programa de Shows y Entradas")
            break
        case _:
            print("Opcion invalida.Debe ingresar una opcion del 1 al 8.")
            break