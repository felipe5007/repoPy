Opciones:
1. Registrar Usuario
2. Iniciar Sesión
3. Mostrar Usuarios Registrados
4. Salir
Solicitamos al usuario que seleccione una opción ingresando un número.


def registrar_usuario():
    usuario = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    usuarios.append({"usuario": usuario, "password": password})
    print("Usuario registrado exitosamente.")


def iniciar_sesion():
    usuario_ingresado = input("Ingrese su nombre de usuario: ")
    contraseña_ingresada = input("Ingrese su contraseña: ")
    for usuario in usuarios:
        if usuario["usuario"] == usuario_ingresado and usuario["contraseña"] == contraseña_ingresada:
            print("Inicio de sesión exitoso.")
            return True
    print("Usuario o contraseña incorrectos.")
    return False

def mostrar_usuarios_registrados():
    for usuario in usuarios:
        print(usuario["usuario"])
        
def salir():
    print("Saliendo del sistema.")
    exit()