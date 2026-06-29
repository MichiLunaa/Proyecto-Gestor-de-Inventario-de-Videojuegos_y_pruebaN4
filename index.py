coleccion = []


def agregar_juego():
    titulo = input("Ingrese título del juego: ")
    plataforma = input("Ingrese plataforma: ")

    try:
        año = int(input("Ingrese año: "))
    except ValueError:
        print("El año debe ser un número.")
        return

    estado = input("Ingrese estado (pendiente/terminado): ")

    juego = {
        "titulo": titulo,
        "plataforma": plataforma,
        "año": año,
        "estado": estado
    }

    coleccion.append(juego)
    print("Juego agregado correctamente.")


def listar_juegos():

    if len(coleccion) == 0:
        print("No hay juegos registrados.")
        return

    for juego in coleccion:
        print("--------------------")
        print("Título:", juego["titulo"])
        print("Plataforma:", juego["plataforma"])
        print("Año:", juego["año"])
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