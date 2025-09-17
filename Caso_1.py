#Caso 1
#La biblioteca escolar necesita un sistema de gestión sencillo para su catálogo de libros y las copias
#disponibles. Se pide desarrollar un programa con una interfaz basada en menú que utilice listas 
#paralelas (una para títulos[] y otra para ejemplares[]). Cada título debe estar vinculado a su 
#número correspondiente de copias utilizando el mismo índice en ambas listas.
#Se debe utilizar un bucle while para navegar por las opciones del menú hasta que el usuario elija salir.

print("Bienvenido a la Biblioteca Escolar")
titulos = []
ejemplares = []
opcion = 0
while opcion != 8:
    print("\nMenú de opciones:")
    print("1. Agregar un nuevo libro")
    print("2. Mostrar catálogo de libros")
    print("3. Buscar un libro")
    print("4. Libros Agotados")
    print("5. Mostrar Catalogo Libros Disponibles")
    print("6. Prestamo de Libros")
    print("7. Devolución de Libros")
    print("8. Salir")
    opcion = int(input("Seleccione una opción (1-9): "))

    if opcion == 1:
        titulo = input("Ingrese el título del libro: ").lower
        num_ejemplares = int(input("Ingrese el número de ejemplares disponibles: "))
        titulos.append(titulo)
        ejemplares.append(num_ejemplares)
        print(f"Libro '{titulo}' con {num_ejemplares} ejemplares agregado al catálogo.")
    elif opcion == 2:
        if not titulos:
            print("El catálogo está vacío.")
        else:
            print("\nCatálogo de libros:")
            for i in range(len(titulos)):
                print(f"{i + 1}. {titulos[i]} - Ejemplares disponibles: {ejemplares[i]}")
    elif opcion == 3:
        buscar = input("Ingrese el título del libro a buscar: ").lower
        if buscar in titulos:
            indice = titulos.index(buscar)
            print(f"El libro '{buscar}' está disponible con {ejemplares[indice]} ejemplares.")
        else:
            print(f"El libro '{buscar}' no se encuentra en el catálogo.")
    elif opcion == 4:
        print("\nLibros agotados:")
        for i in range(len(titulos)):
            if ejemplares[i] == 0:
                    print(f"{titulos[i]}")
            else:
                print("No hay libros agotados.")
    elif opcion == 5:
        titulo = input("Ingrese el nuevo título del libro: ").lower
        num_ejemplares = int(input("Ingrese el número de ejemplares disponibles: "))
        titulos.append(titulo)
        ejemplares.append(num_ejemplares)
        print(f"Libro '{titulo}' con {num_ejemplares} ejemplares agregado al catálogo.")
    elif opcion == 6:
        prestamo=input("Ingresar el titulo del libro a prestar: ").lower
        if prestamo in titulos:
            indice_prestamo = titulos.index(prestamo)
            if ejemplares[indice_prestamo] > 0:
                ejemplares[indice_prestamo] -= 1
                print(f"Has prestado el libro '{prestamo}'. Ejemplares restantes: {ejemplares[indice_prestamo]}")
            else:
                print(f"Lo siento, no hay ejemplares disponibles del libro '{prestamo}'.")
    elif opcion == 7:
        devolucion=input("Ingresar el titulo del libro a devolver: ").lower
        if devolucion in titulos:
            indice_devolucion = titulos.index(devolucion)
            ejemplares[indice_devolucion] += 1
            print(f"Has devuelto el libro '{devolucion}'. Ejemplares disponibles: {ejemplares[indice_devolucion]}")