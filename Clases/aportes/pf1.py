#trabajar con el sistema de archivos
import os 

# Función para registrar usuarios
def registrar_usuario(usuario, contrasena, base_de_datos):
    base_de_datos[usuario] = contrasena

# Función para mostrar la información de usuarios
def mostrar_usuarios(base_de_datos):
    for usuario, contrasena in base_de_datos.items():
        print(f"Usuario: {usuario}, Contraseña: {contrasena}")

# Función para iniciar sesión
def iniciar_sesion(usuario, contrasena, base_de_datos):
    try:
        stored_password = base_de_datos[usuario]
        if stored_password == contrasena:
            print("Inicio de sesión exitoso.")
        else:
            print("Contraseña incorrecta.")
    except KeyError:
        print("Usuario no encontrado.")

# Función para guardar usuarios en un archivo de texto
def guardar_usuarios_en_archivo(base_de_datos, archivo):
    with open(archivo, 'w') as f:
        for usuario, contrasena in base_de_datos.items():
            f.write(f"{usuario}:{contrasena}\n")

# Función para cargar usuarios desde un archivo de texto
def cargar_usuarios_desde_archivo(archivo):
    base_de_datos = {}
    if os.path.exists(archivo):
        with open(archivo, 'r') as f:
            lines = f.readlines()
            for line in lines:
                parts = line.strip().split(':')
                if len(parts) == 2:
                    usuario, contrasena = parts
                    base_de_datos[usuario] = contrasena
    return base_de_datos

# Diccionario para almacenar usuarios y contraseñas
usuarios_base_de_datos = {}

# Cargar usuarios desde un archivo (si existe)
usuarios_base_de_datos = cargar_usuarios_desde_archivo('usuarios.txt')

while True:
    print("\nOpciones:")
    print("1. Registrar Usuario")
    print("2. Iniciar Sesión")
    print("3. Mostrar Usuarios Registrados")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        usuario = input("Ingrese el nombre de usuario: ")
        contrasena = input("Ingrese la contraseña: ")
        registrar_usuario(usuario, contrasena, usuarios_base_de_datos)
        guardar_usuarios_en_archivo(usuarios_base_de_datos, 'usuarios.txt')
        print("Usuario registrado exitosamente.")
    elif opcion == '2':
        usuario = input("Ingrese el nombre de usuario: ")
        contrasena = input("Ingrese la contraseña: ")
        iniciar_sesion(usuario, contrasena, usuarios_base_de_datos)
    elif opcion == '3':
        mostrar_usuarios(usuarios_base_de_datos)
    elif opcion == '4':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")