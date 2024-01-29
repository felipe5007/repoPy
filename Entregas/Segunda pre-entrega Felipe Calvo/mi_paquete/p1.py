from google.colab import drive
drive.mount("/drive/")
BD = "/drive/folders/1f5owoAerhR9yXm6ZN6cMiru7MGlIgv_J"

BD = {}

# Función para guardar la información en un archivo de texto en Google Drive
def guardar_en_google_drive(BD):
    content = "Usuarios registrados:\n"
    for usuario, datos in BD.items():
        nombre_completo = datos['nombre_completo']
        password = datos['contrasena']
        content += f"Nombre completo: {nombre_completo}, Usuario: {usuario}, Contraseña: {password}\n"

    # Crea un archivo de texto en Google Drive
    file = drive.CreateFile({'title': 'BD.txt'})
    file.Upload()

    # Escribe el contenido en el archivo
    file.SetContentString(content)
    file.Upload()

    print("Información guardada correctamente en Google Drive")
    
    # Función para validar una contraseña
def validar_password(password):
    if len(password) < 6:
        return False, "La contraseña debe tener al menos 6 caracteres."
    if not any(c.isalpha() for c in password):
        return False, "La contraseña debe contener al menos una letra."
    if not any(c.isdigit() for c in password):
        return False, "La contraseña debe contener al menos un número."
    return True, "Contraseña válida."


# Función para registrar un usuario, contraseña y nombre completo
def registrar_user(BD, user, password, nombre_completo):
    # Add the user to the database
    BD[user] = {
        "nombre_completo": nombre_completo,
        "password": password,
    }

    if user in BD:
        print("El usuario ya está registrado en nuestra Base de Datos. Intente con otro Nick")
    else:
        while True:
            password = input("Ingrese contraseña: ")
            confirmacion = input("Confirme la contraseña: ")
            password_valida, mensaje = validar_password(password)

            if password != confirmacion:
                print("Las contraseñas no coinciden. Intente de nuevo.")
            elif not password_valida:
                print(mensaje)
            else:
                # Si todas las validaciones pasan, se registra el usuario
                if user in BD:
                    print("Contraseña anterior eliminada.")
                    del BD[user]['contrasena']
                BD[user] = {'contrasena': password, 'nombre_completo': nombre_completo}
                print("Usuario registrado con éxito.")
                guardar_en_google_drive(BD)  # Guardar automáticamente en el archivo
                break

# Función para mostrar la información de usuarios registrados
def mostrar_user(BD):
    if not BD:
        print("No hay usuarios registrados.")
    else:
        print("Usuarios registrados:")
        for user, datos in BD.items():
            nombre_completo = datos['nombre_completo']
            password = datos['password']
            print(f"Nombre completo: {nombre_completo} | Usuario: {user} | Contraseña: {password}")

# Función para realizar el login de un usuario
def login(BD, user):
    if user in BD:
        nombre_completo = BD[user]['nombre_completo']
        intentos = 0  # Contador de intentos incorrectos
        while intentos < 3:
            password = input("Ingrese contraseña: ")
            if BD[user]['password'] == password:
                print(f"¡Bienvenido {nombre_completo} !")
                return  # Salir del bucle si la contraseña es correcta
            else:
                intentos += 1
                print(f"Contraseña incorrecta. Intento {intentos} de 3.")
        # Si se ingresó incorrectamente la contraseña 3 veces, bloquear la cuenta
        print("Has ingresado incorrectamente la contraseña 3 veces.")
        opcion = input("¿Restablecer contraseña? (S/N): ").strip().lower()
        if opcion == 's':
            nueva_password = input("Ingrese la nueva contraseña: ")
            BD[user]['contrasena'] = nueva_password
            print("Contraseña restablecida con éxito.")
            guardar_en_google_drive(BD)  # Actualizar la contraseña en el archivo
        else:
            print("Acceso denegado. La contraseña anterior se mantendrá.")
    else:
        print("Usuario no registrado.")
        
# Función para buscar usuarios por nombre o nombre completo
def buscar_user(BD, nombre):
    print("Usuarios encontrados:")
    encontrado = False
    for user, datos in BD.items():
        if nombre in datos['nombre_completo'] or nombre == user:
            password = datos['contrasena']
            print(f"Nombre Completo: {datos['nombre_completo']}| Nombre de Usuario: {user}| Contraseña: {password}")
            encontrado = True
    if not encontrado:
        print(f"No se encontraron usuarios con el nombre de usuario/nombre completo:  {user} ")

def ver_user():
    print("Lista de usuarios: ")
    for user, datos in BD.items():
        print(f"Usuario: {user}, Contraseña: {datos['contrasena']}")
    
# Función para mostrar la información de usuarios registrados
def mostrar_user(BD):
    if not BD:
        print("No hay usuarios registrados.")
    else:
        print("Usuarios registrados:")
        for user, datos in BD.items():
            nombre_completo = datos['nombre_completo']
            password = datos['contrasena']
            print(f"Nombre completo: {nombre_completo} | Usuario: {user} | Contraseña: {password}")

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
        user = input("Ingrese nombre de usuario: ")
        password = input("Ingrese contraseña: ")
        registrar_user(BD,user, password, nombre_completo)

    elif opcion == "2":
        user = input("Ingrese nombre de usuario: ")
        password = input("Ingrese contraseña: ")
        login(BD, user)

    elif opcion == "3":
        guardar_en_google_drive(BD)

    elif opcion == "4":
        nombre = input("Ingrese el nombre a buscar: ")
        buscar_user(BD, nombre)

    elif opcion == "5":
        mostrar_user(BD)

    elif opcion == "6":
        print("Hasta Pronto!!!")
        break

    else:
        print("Opción no válida. Intente de nuevo.")