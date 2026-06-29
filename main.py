from index import agregar_juego
from index import listar_juegos
from index import estadisticas
from index import cambiar_estado
from index import guardar_datos
from index import cargar_datos
from index import recomendacion

cargar_datos()

while True:

    print("\n====== COLECCIONISTA DE JUEGOS ======")
    print("1. Agregar juego")
    print("2. Listar colección")
    print("3. Ver estadísticas")
    print("4. Cambiar estado")
    print("5. Recomendación del día")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_juego()

    elif opcion == "2":
        listar_juegos()

    elif opcion == "3":
        estadisticas()

    elif opcion == "4":
        cambiar_estado()

    elif opcion == "5":
        recomendacion()

    elif opcion == "6":

        guardar_datos()

        print("Programa finalizado.")
        break

    else:

        print("Opción inválida.")