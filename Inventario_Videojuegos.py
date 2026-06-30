import json
import os
import requests 

coleccion = []

def agregar_juego():
    titulo = input("Ingrese título del juego: ")
    plataforma = input("Ingrese plataforma: ")

    try:
        anio = int(input("Ingrese año: "))
    except ValueError:
        print("El año debe ser un número.")
        return

    estado = input("Ingrese estado (pendiente/terminado): ")

    juego = {
        "titulo": titulo,
        "plataforma": plataforma,
        "anio": anio,
        "estado": estado
    }

    coleccion.append(juego)
    print("Juego agregado correctamente.")


def listar_juegos():
    if len(coleccion) == 0:
        print("No hay juegos registrados.")
        return
    for juego in coleccion:
        print("---------------------------")
        print("Título:", juego["titulo"])
        print("Plataforma:", juego["plataforma"])
        print("Año:", juego["anio"])
        print("Estado:", juego["estado"])

def estadisticas():
    pendientes = 0
    for juego in coleccion:
        if juego["estado"].lower() == "pendiente":
            pendientes += 1

    print("Juegos registrados:", len(coleccion))
    print("Juegos pendientes:", pendientes)


def cambiar_estado():
    titulo = input("Ingrese el título del juego: ")
    encontrado = False
    for juego in coleccion:

        if juego["titulo"].lower() == titulo.lower():

            print("Estado actual:", juego["estado"])

            nuevo_estado = input("Nuevo estado (pendiente/terminado): ")

            juego["estado"] = nuevo_estado

            print("Estado actualizado.")

            encontrado = True
            break

    if encontrado == False:
        print("Juego no encontrado.")

def guardar_datos():
    with open("coleccion.json", "w") as archivo:
        json.dump(coleccion, archivo, indent=4)

    print("Datos guardados correctamente.")

def cargar_datos():
    global coleccion
    if os.path.exists("coleccion.json"):
        with open("coleccion.json", "r") as archivo:
            coleccion = json.load(archivo)

def recomendacion():
    try:
        respuesta = requests.get("https://www.freetogame.com/api/games")
        if respuesta.status_code == 200:
            juegos = respuesta.json()
            print("\n===== RECOMENDACIÓN DEL DÍA =====")
            print("Título:", juegos[0]["title"])
            print("Género:", juegos[0]["genre"])
            print("Plataforma:", juegos[0]["platform"])
        else:
            print("No fue posible obtener una recomendación.")
    except:
        print("No se pudo conectar con la API.")

def main():
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
main()
