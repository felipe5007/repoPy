def registrar_usuario():
print(“Registro de nuevo usuario”)
nombre \= input(“Nombre: “)
apellido \= input(“Apellido: “)
usuario \= input(“Nombre de usuario: “)
# Verificar si el usuario ya existe
if usuario in base_de_datos_usuarios:
print(“El usuario ya existe. Por favor, elige otro nombre de usuario.”)

return