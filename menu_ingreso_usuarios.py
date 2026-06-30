
usuarios = {}

def validar_sexo():
  while True:
    sexo = input("Ingrese sexo: ")
    if sexo == 'M' or sexo == 'F':
      return sexo
    else:
      print("Debe ingresar M o F solamente. Intente de nuevo.")

def validar_contrasena():
  while True:
    clave = input("Ingrese contraseña: ")
    if len(clave) < 8:
      print("Contraseña no valida. Intente otra.")
      continue
    if " " in clave:
      print("Contraseña no valida. Intente otra.")
      continue
    tiene_letra = False
    tiene_numero = False
    for caracter in clave:
      if caracter.isalpha():
        tiene_letra = True
      if caracter.isdigit():
        tiene_numero = True
    if tiene_letra and tiene_numero:
      print("Contraseña valida.")
      return clave
    else:
      print("Contraseña no valida. Intente otra.")

def ingresar_usuario():
  while True:
    nombre = input("Ingrese nombre de usuario: ")
    if nombre in usuarios:
      print("Usuario ya existe. Intente otro.")
    else:
      break
  sexo = validar_sexo()
  contrasena = validar_contrasena()
  usuarios[nombre] = {
    'sexo': sexo,
    'contraseña': contrasena
  }
  print("Usuario ingresado con exito!!")

def buscar_usuario():
  nombre = input("Ingrese usuario a buscar: ")
  if nombre in usuarios:
    sexo = usuarios[nombre]['sexo']
    clave = usuarios[nombre]['contraseña']
    print("El sexo del usuario es: ", sexo,"y la contraseña es: ", clave)
  else:
    print("El usuario no se encuentra.")

def eliminar_usuario():
  nombre = input("Ingrese usuario a buscar: ")
  if nombre in usuarios:
    del usuarios[nombre]
    print("Usuario eliminado con éxito!")
  else:
    print("No se pudo eliminar usuario!")

def main():
  while True:
    print("MENÚ PRINCIPAL")
    print("1.- Ingresar usuario.")
    print("2.- Buscar usuario.")
    print("3.- Eliminar usuario.")
    print("4.- Salir.")
     
    opcion = input("Ingrese opción: ")
    if opcion == "1":
      ingresar_usuario()
    elif opcion == "2":
      buscar_usuario()
    elif opcion == "3":
      eliminar_usuario()
    elif opcion == "4":
      print("Programa terminado...")
      break
    else:
      print("Debe ingresar una opción válida!!")

main()