from claseViajeroFrecuente import ViajeroFrecuente

if __name__ == '__main__':
 with open("viajeros.txt") as f:
    lineas = f.readlines()
    viajeros = []
    for linea in lineas:
        datos = linea.strip().split(",")
        viajero = ViajeroFrecuente(int(datos[0]), datos[1], datos[2], datos[3], int(datos[4]))
        viajeros.append(viajero)

num_viajero = int(input("Ingrese el número de viajero frecuente: "))
viajero = None
for v in viajeros:
    if v.num_viajero == num_viajero:
        viajero = v
        break

if viajero is not None:
    opcion = ""
    while opcion != "d":
        print("Menú de opciones:")
        print("a- Consultar Cantidad de Millas")
        print("b- Acumular Millas")
        print("c- Canjear Millas")
        print("d- Salir")
        opcion = input("Ingrese la opción deseada: ")
        
        if opcion == "a":
            print("Cantidad de millas acumuladas:", viajero.cantidadTotaldeMillas())
        elif opcion == "b":
            millas_recorridas = int(input("Ingrese la cantidad de millas recorridas: "))
            print("Millas acumuladas después de la operación:", viajero.acumularMillas(millas_recorridas))
        elif opcion == "c":
            millas_a_canjear = int(input("Ingrese la cantidad de millas a canjear: "))
            print("Millas acumuladas después de la operación:", viajero.canjearMillas(millas_a_canjear))
        elif opcion == "d":
            print("Saliendo del programa...")
        else:
            print("Opción inválida.")
else:
    print("No se encontró un viajero frecuente con ese número.")
