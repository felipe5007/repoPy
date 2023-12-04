Importamos el módulo os para trabajar con el sistema de archivos.

Definimos una función llamada registrar_usuario que toma tres argumentos: usuario (nombre de usuario), 
contrasena (contraseña)y base_de_datos. Esta función agrega una entrada al diccionario base_de_datos 
donde la clave es el nombre de usuario y el valor es la contraseña.

Definimos una función llamada mostrar_usuarios que toma un argumento base_de_datos. Esta función itera 
a través del diccionario base_de_datos e imprime el nombre de usuario y la contraseña de cada usuario registrado.

Definimos una función llamada iniciar_sesion que toma tres argumentos: usuario (nombre de usuario), 
contrasena (contraseña) y base_de_datos. Esta función intenta obtener la contraseña almacenada en el 
diccionario base_de_datos para el usuario proporcionado. Luego, compara la contraseña almacenada con la 
contraseña ingresada y muestra un mensaje apropiado en función del resultado.

Definimos una función llamada guardar_usuarios_en_archivo que toma dos argumentos: base_de_datos y archivo. 
Esta función guarda los usuarios y contraseñas almacenados en el diccionario base_de_datos en un archivo de 
texto llamado archivo. Los datos se almacenan en el formato "usuario:contraseña" en líneas separadas.

Definimos una función llamada cargar_usuarios_desde_archivo que toma un argumento archivo. Esta función 
carga usuarios y contraseñas desde un archivo de texto llamado archivo y los devuelve como un diccionario. 
Si el archivo no existe, devuelve un diccionario vacío.

Creamos un diccionario llamado usuarios_base_de_datos para almacenar usuarios y contraseñas.

Cargamos usuarios y contraseñas existentes desde el archivo "usuarios.txt" (si existe) y los almacenamos 
en usuarios_base_de_datos usando la función cargar_usuarios_desde_archivo.

Iniciamos un bucle infinito (while True) para mostrar el menú principal del programa.

Mostramos las opciones del menú:

markdown
Copy code
Opciones:
1. Registrar Usuario
2. Iniciar Sesión
3. Mostrar Usuarios Registrados
4. Salir
Solicitamos al usuario que seleccione una opción ingresando un número.

Si el usuario elige la opción '1' (Registrar Usuario):

Solicitamos al usuario que ingrese un nombre de usuario y una contraseña.
Llamamos a la función registrar_usuario para registrar al usuario en usuarios_base_de_datos.
Llamamos a la función guardar_usuarios_en_archivo para guardar los cambios en el archivo "usuarios.txt".
Mostramos un mensaje de confirmación.
Si el usuario elige la opción '2' (Iniciar Sesión):

Solicitamos al usuario que ingrese un nombre de usuario y una contraseña.
Llamamos a la función iniciar_sesion para verificar si el inicio de sesión es exitoso.
Si el usuario elige la opción '3' (Mostrar Usuarios Registrados):

Llamamos a la función mostrar_usuarios para mostrar la información de los usuarios registrados en usuarios_base_de_datos.
Si el usuario elige la opción '4' (Salir):

Imprimimos un mensaje de despedida y salimos del bucle while usando break.
Si el usuario ingresa una opción no válida, mostramos un mensaje de error.

Este programa permite registrar usuarios, iniciar sesión, mostrar usuarios registrados y guardar los datos en un archivo de texto para persistencia.