#RESTAURANTE-Platos del día y porciones

platos=[]
porciones=[]
opciones=[1,2,3,4,5,6,7,8]
opc=0

while opc!=8:
    print("\n Menú RESTAURANTE")
    print("1.Ingresar lista de platos.")
    print("2.Ingresar porciones disponibles.")
    print("3.Mostrar platos con porciones.")
    print("4.Consultar porciones de un plato")
    print("5.Lista de platos agotados.")
    print("6.Agregar plato.")
    print("7.Vender/Devolver porciones.")
    print("8.Salir del menú.")

    opc=input("\n Ingrese una opcion: ")

    while not opc.isdigit(): #Validacion opcion numerica
        opc=input("Opcion invalida. Intente de nuevo: ")
        continue
        
    opc=int(opc)

    match opc:
        case 1: #Ingreso del platos,se limpia cada vez que usan esta opcion
            platos.clear()
            cantidad=input("\n Ingrese la cantidad de platos que desea cargar: ")

            while not cantidad.isdigit():
                cantidad=input("\n Cantidad invalida. Ingrese cantidad: ")
                continue
            
            cantidad=int(cantidad) 

            for i in range(cantidad):
                plato=input(f"\n Ingrese el plato {i+1}: ").title()

                while plato=="" or plato in platos:
                    plato=input("\n Plato vacio o duplicado. Ingrese un plato valido: ")

                platos.append(plato)            

        case 2: #Ingreso porciones por plato
                porciones.clear()
                if len(platos)==0:
                    print("Primero debe ingresar platos.")
                else:
                    for i in range(len(platos)):
                        porcion=input(f"Cantidad de porciones de {platos[i]}: ")
                        while not porcion.isdigit(): #Validacion opcion numerica
                            porcion=input(f"Opcion invalida. Cantidad de porciones de {platos[i]}: ")
                            continue
                        porciones.append(int(porcion))
        
        case 3: #Mostrar Listado de Patos con porciones
            if len(platos)==0:
                print("\nPrimero debe ingresar los platos.")
            elif len(porciones) != len(platos):
                print("\nDebe ingresar la cantidad de porciones de cada plato.")
            else:
                print("\nMenu de platos con sus respectivas porciones")
                for i in range(len(platos)):
                    print(f"{platos[i]}: {porciones[i]} porciones")

        case 4: #Consultar porciones de un plato
            if not platos:
                print("\n NO hay platos ingresados")
            elif not porciones:
                print("\n Debe ingresar las porciones de cada plato")
            else:
                plato=input("\n Ingrese el plato que desea consultar: ").title()
                if plato in platos:
                    indice=platos.index(plato)
                    print(f"\n {platos[indice]} - {porciones[indice]} porciones")
                else:
                    print("\n Plato no encontrado.")

        case 5: #Lista de platos agostados
            if len(platos)==0:
                print("\n No hay platos igresados")
            elif len(porciones)==0:
                print("\n Primero debe cargar las porciones que tiene cada plato.")
            elif 0 in porciones:
                print("\nPlatos agostados:")
                for i in range(len(platos)):
                    if porciones[i]==0:
                        print(f"{platos[i]}")

        case 6: #Agregar nuevo plato
            plato=input("\nIngrese el nuevo plato: ").title()
            while plato=="" or plato in platos:
                plato=input("\nPlato invalido o duplicado. Ingrese de nuevo: ")
            
            platos.append(plato)
            porcion=input(f"\nPorciones de {plato}: ")
            while not porcion.isdigit(): #Validacion opcion numerica
                porcion=input("\nPorcion invalida. Intente de nuevo: ")
                continue
            porciones.append(int(porcion))

        case 7: #Vender/Devolver porciones
            if len(platos)==0:
                print("\nPrimero debe ingresar los platos.")
            elif len(porciones) != len(platos):
                print("\nDebe ingresar la cantidad de porciones de cada plato.")
            else:
                print("\nAccion que desea realizar:")
                print("1.Vender porcion")
                print("2.Devolver porcion")
                accion=input("Ingrese la opcion elegida (1 o 2 ): ")
                plato=input("Ingrese plato: ").title()
                
                if plato in platos:
                    cant=int(input("Cantidad de platos para accionar: "))
                    
                    indi=platos.index(plato)

                    if accion=="1": #Vender -1
                        if cant<=0:
                                print("Debe vender almenos una porcion.")
                        elif cant>porciones[indi]:
                                print("Cantidad de porciones insuficientes para la venta.")
                        else:
                            porciones[indi] -= cant
                            print(f"Venta realizada. Quedan {porciones[indi]} porciones de {platos[indi]}")
                    elif accion=="2": #Devolver +1
                            if cant<=0:
                                print("Debe devolver almenos una porcion.")
                            else:
                                porciones[indi] += cant
                                print(f"Devolucion realizada. Quedan {porciones[indi]} porciones de {platos[indi]}")
                    else:
                        print("Opcion invalida")
                else:
                    print("Plato invalido o no encontrado")
        case 8: #Salir
            break
        case _: #Opcion invalida
            print("\n Opcion invalida. Intente de nuevo.")

print("\n Gracias por utilizar el sistema del RESTAURANTE.")