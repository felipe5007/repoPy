# Importa las bibliotecas necesarias
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import getpass

import os

# Directorio donde se encuentra el archivo client_secrets.json
secrets_file_dir = 'S:\4-SEBASTIAN MORONI\06. EDUCACION\02. PROGRAMACION\04. Programación con PYTHON - CODERHOUSE\Practicas\Hacia el Proyecto\client_secrets.json'

# Construye la ruta completa al archivo client_secrets.json
secrets_file_path = os.path.join(secrets_file_dir, '.\client_secrets.json')

# Luego, utiliza secrets_file_path en tu código

# Configura la autenticación de Google Drive
gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # Abre una ventana del navegador para autenticarse
drive = GoogleDrive(gauth)


# Función para validar una contraseña
def validar_contrasenia(contrasenia):
    if len(contrasenia) < 6:
        return False, "La contraseña debe tener al menos 6 caracteres."
    if not any(c.isalpha() for c in contrasenia):
        return False, "La contraseña debe contener al menos una letra."
    if not any(c.isdigit() for c in contrasenia):
        return False, "La contraseña debe contener al menos un número."
    return True, "Contraseña válida."



# Función para registrar un usuario, contraseña y nombre completo
def registrar_usuario(database, usuario, contrasenia, nombre_completo):
    if usuario in database:
        print("El usuario ya está registrado en nuestra Base de Datos. Intente con otro Nick")
    else:
        while True:
            contrasenia = input("Ingrese contraseña: ")
            confirmacion = input("Confirme la contraseña: ")

            contrasenia_valida, mensaje = validar_contrasenia(contrasenia)

            if contrasenia != confirmacion:
                print("Las contraseñas no coinciden. Intente de nuevo.")
            elif not contrasenia_valida:
                print(mensaje)
            else:
                # Si todas las validaciones pasan, se registra el usuario
                if usuario in database:
                    print("Contraseña anterior eliminada.")
                    del database[usuario]['contrasena']
                database[usuario] = {'contrasena': contrasenia, 'nombre_completo': nombre_completo}
                print("Usuario registrado con éxito.")
                guardar_en_google_drive(database)  # Guardar automáticamente en el archivo
                break
            
            
            
            
            
# Función para mostrar la información de usuarios registrados
def mostrar_usuarios(database):
    if not database:
        print("No hay usuarios registrados.")
    else:
        print("Usuarios registrados:")
        for usuario, datos in database.items():
            nombre_completo = datos['nombre_completo']
            contrasenia = datos['contrasena']
            print(f"Nombre completo: {nombre_completo} | Usuario: {usuario} | Contraseña: {contrasenia}")




# Función para realizar el login de un usuario
def login(database, usuario):
    if usuario in database:
        intentos = 0  # Contador de intentos incorrectos
        while intentos < 3:
            contrasenia = input("Ingrese contraseña: ")
            if database[usuario]['contrasena'] == contrasenia:
                print(f"¡Bienvenido {nombre_completo} !")
                return  # Salir del bucle si la contraseña es correcta
            else:
                intentos += 1
                print(f"Contraseña incorrecta. Intento {intentos} de 3.")
        
        # Si se ingresó incorrectamente la contraseña 3 veces, bloquear la cuenta
        print("Has ingresado incorrectamente la contraseña 3 veces.")
        opcion = input("¿Restablecer contraseña? (S/N): ").strip().lower()
        if opcion == 's':
            nueva_contrasenia = input("Ingrese la nueva contraseña: ")
            database[usuario]['contrasena'] = nueva_contrasenia
            print("Contraseña restablecida con éxito.")
            guardar_en_google_drive(database)  # Actualizar la contraseña en el archivo
        else:
            print("Acceso denegado. La contraseña anterior se mantendrá.")
    else:
        print("Usuario no registrado.")



# Función para guardar la información en un archivo de texto en Google Drive
def guardar_en_google_drive(database):
    content = "Usuarios registrados:\n"
    for usuario, datos in database.items():
        nombre_completo = datos['nombre_completo']
        contrasenia = datos['contrasena']
        content += f"Nombre completo: {nombre_completo}, Usuario: {usuario}, Contraseña: {contrasenia}\n"

    # Crea un archivo de texto en Google Drive
    file = drive.CreateFile({'title': 'usuarios.txt'})
    file.Upload()

    # Escribe el contenido en el archivo
    file.SetContentString(content)
    file.Upload()

    print("Información guardada correctamente en Google Drive")
            
            
            
            

# Función para buscar usuarios por nombre o nombre completo
def buscar_usuario(database, nombre):
    print("Usuarios encontrados:")
    encontrado = False
    for usuario, datos in database.items():
        if nombre in datos['nombre_completo'] or nombre == usuario:
            contrasenia = datos['contrasena']
            print(f"Nombre Completo: {datos['nombre_completo']}| Nombre de Usuario: {usuario}| Contraseña: {contrasenia}")
            encontrado = True

    if not encontrado:
        print(f"No se encontraron usuarios con el nombre de usuario/nombre completo:  {nombre} ")
        
        
        

# Base de datos de usuarios (diccionario)
database = {}


#Menú de la aplicación 
while True:
    print("\n-")
    print("---------------------------")
    print("    MENÚ PRINCIPAL")
    print("---------------------------")
    print("\n")
    print("1. Registrarse como usuario")
    print("2. Login")
    print("3. Guardar Información en Base de Datos")
    print("4. Buscar usuarios por nombre")
    print("5. Mostrar usuarios registrados")
    print("6. Salir")
    print("================================")
    opcion = input("Seleccione la Opción deseada: ")

    if opcion == "1":
        nombre_completo = input("Ingrese su nombre completo (nombre y apellido): ")
        usuario = input("Ingrese nombre de usuario: ")
        contrasenia = ""
        registrar_usuario(database, usuario, contrasenia, nombre_completo)

    elif opcion == "2":
        usuario = input("Ingrese nombre de usuario: ")
        #contrasenia = input("Ingrese contraseña: ")
        login(database, usuario)

    elif opcion == "3":
        guardar_en_google_drive(database)

    elif opcion == "4":
        nombre = input("Ingrese el nombre a buscar: ")
        buscar_usuario(database, nombre)

    elif opcion == "5":
        mostrar_usuarios(database)

    elif opcion == "6":
        print("Hasta Pronto!!!")
        break

    else:
        print("Opción no válida. Intente de nuevo.")