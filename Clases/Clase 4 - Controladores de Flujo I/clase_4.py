# UML
# https://es.wikipedia.org/wiki/Lenguaje_unificado_de_modelado


# if, multiples if

# if <condicion a cumplirse>:
#     <bloque de codigo a ejecuarse si la condicion se cumple>


# if True:
#     print('Hola, empece con los if')
#     a = 15
#     b = 14
#     print(a+b)
# print('mas codigo')

# if False:
#     print('No deberia aparecer')


# primer_numero = int(input('Ingrese una numero: '))
# segundo_numero = int(input('Ingrese otro numero: '))
    
# if primer_numero < segundo_numero:
#     print('El primer valor es menor al segundo')

# if primer_numero > segundo_numero:
#     print('El primer valor es mayor al segundo')
#     print('Y tambien muestro esto porque sigo estando en el mismo bloque de codigo')

# if primer_numero == segundo_numero:
#     print('Ambos valores son iguales')

# if primer_numero < segundo_numero and primer_numero != segundo_numero - 5:
#     print('Se cumplio la condicion compleja')

# print('Estoy fuera de los if')


# Anidado de if

# primer_numero = int(input('Ingrese una numero: '))
# segundo_numero = int(input('Ingrese otro numero: '))

# if primer_numero < segundo_numero:
#     print('primer_numero es menor')
#     if primer_numero == segundo_numero - 3:
#         print('primer_numero es igual a segundo_numero menos 3')
#     print('Sali del if anidado')


# else

# if <condicion>:
#     pass # ...
# else:
#     ...

# primer_numero = int(input('Ingrese una numero: '))
# segundo_numero = int(input('Ingrese otro numero: '))

# v1
# if primer_numero < segundo_numero:
#     print('El primer valor es menor al segundo')

# if primer_numero > segundo_numero and primer_numero == segundo_numero:
#     print('primer_numero no es menor a segundo')

# v2
# if primer_numero < segundo_numero:
#     print('El primer valor es menor al segundo')

# if not (primer_numero < segundo_numero):
#     print('primer_numero no es menor a segundo')
   
# v3 Final 
# if primer_numero < segundo_numero:
#     print('El primer valor es menor al segundo')
# else:
#     print('primer_numero no es menor a segundo')
    
    
# ej1:
# primer_numero = int(input('Ingrese una numero: '))
# segundo_numero = int(input('Ingrese otro numero: '))
# if primer_numero == segundo_numero:
#     print('son iguales')
# else:
#     print('no son iguales')

# print('Estoy fuera de los if')


# ej2:
# var = 15
# primer_numero = int(input('Ingrese una numero: '))
# segundo_numero = int(input('Ingrese otro numero: '))

# if primer_numero == segundo_numero:
#     print('son iguales')
#     if primer_numero < var:
#         print('son menores a var')
#     else:
#         print('son mayores a var')
# else:
#     print('no son iguales')

# print('Estoy fuera de los if')


# if False:
#     print('Hola')
# if True:
#     print('True')
# else:
#     print('pase por el else')


# ej3:
# var = 15
# primer_numero = int(input('Ingrese una numero: '))
# segundo_numero = int(input('Ingrese otro numero: '))

# if primer_numero == segundo_numero:
#     print('son iguales')
#     if primer_numero < var:
#         print('son menores a var')
#     else:
#         print('son mayores a var')
# else:
#     print('no son iguales')
#     if primer_numero < var:
#         print('primer_numero es menor a var')
#         if segundo_numero < var:
#             print('segndo_numero es menor a var')
#         else:
#             print('segndo_numero es mayor a var')
#     else:
#         print('primer_numero es mayor a var')

# print('Estoy fuera de los if')


# ej4
# contrasenia = 'pass123456'
# pass_ingresada = input('Ingresa la contraseña: ')

# if contrasenia == pass_ingresada:
#     print('La contrasenia es correcta! :)')
# else: 
#     print('La contrasenia es incorrecta. :(')

# if if/else en la misma lineas

# contrasenia = 'pass123456'
# pass_ingresada = input('Ingresa la contraseña: ')
# if contrasenia == pass_ingresada: print('La contrasenia es correcta! :)')

# v1
# if contrasenia == pass_ingresada: print('La contrasenia es correcta! :)')
# else: print('La contrasenia es incorrecta. :(')

# v2
# print('La contrasenia es correcta! :)') if contrasenia == pass_ingresada else print('La contrasenia es incorrecta. :(')

# elif

# primer_numero = int(input('Ingrese una numero: '))
# segundo_numero = int(input('Ingrese otro numero: '))
    
    
# if primer_numero == segundo_numero - 3:
#     print('El primero es igual al segundo menos 3')
# else:
#     print('El primero es menor al segundo')
    
# if primer_numero == segundo_numero - 3:
#     print('El primero es igual al segundo menos 3')
# if primer_numero < segundo_numero:
#     print('El primero es menor al segundo')
    
# if primer_numero == segundo_numero - 3:
#     print('El primero es igual al segundo menos 3')
# elif primer_numero < segundo_numero:
#     print('El primero es menor al segundo')


# Ej 2

# primer_numero = int(input('Ingrese una numero: '))
# segundo_numero = int(input('Ingrese otro numero: '))

# v1
# if primer_numero < segundo_numero:
#     print('El primer valor es menor al segundo')

# if primer_numero > segundo_numero:
#     print('El primer valor es mayor al segundo')
#     print('Y tambien muestro esto porque sigo estando en el mismo bloque de codigo')

# if primer_numero == segundo_numero:
#     print('Ambos valores son iguales')

# v2
# if primer_numero < segundo_numero:
#     print('primer_numero es menor que segundo_numero')
# elif primer_numero == segundo_numero:
#     print('son iguales')
# else:
#     print('segundo_numero es menor que primer_numero')
    
# v3
# if primer_numero < segundo_numero:
#     print('primer_numero es menor que segundo_numero')
# elif primer_numero == segundo_numero:
#     print('son iguales')
# elif primer_numero > segundo_numero:
#     print('segundo_numero es menor que primer_numero')

# ====================================================================
# ====================================================================
# ====================================================================
# ====================================================================


# primer_numero = int(input('Ingrese una numero: '))

# if primer_numero < 20:
#     print('es menor a 20')
# if primer_numero < 30:
#     print('es menor a 30')
# if primer_numero < 40:
#     print('es menor a 40')
# if primer_numero < 50:
#     print('es menor a 50')

# if primer_numero < 50:
#     print('es menor a 50')
#     if primer_numero < 40:
#         print('es menor a 40')
#         if primer_numero < 30:
#             print('es menor a 30')
#             if primer_numero < 20:
#                 print('es menor a 20')


# if primer_numero < 20:
#     print('es menor a 20')
# elif primer_numero < 30:
#     print('es menor a 30')
# elif primer_numero < 40:
#     print('es menor a 40')
# elif primer_numero < 50:
#     print('es menor a 50')
# else:
#     print('no se cumplio ninguna condicion de las anteriores')


# if True:
#     print('Hola')
# if False:
#     print('True')
# elif False:
#     print('Entre en el primer elif')
# else:
#     print('pase por el else')


# if True:
#     ...
# elif True:
#     ...
# else:
#     ...
    

# if True:
#     ...


# if True:
#     ...
# else:
#    ... 


# if True:
#     ...
# elif True:
#     ...

# nota = 15
# if nota < 4:
#     print('malo')
# elif nota < 7:
#     print('bueno')
# elif nota < 9:
#     print('muy bueno')
# elif nota < 11:
#     print('excelente')
# else:
#     print('pone una nota de 0 a 10')


# primer_numero = int(input('Ingrese una numero: '))
# segundo_numero = int(input('Ingrese otro numero: '))

# if primer_numero < segundo_numero:
#     print('primer_numero es menor que segundo_numero')
# elif primer_numero == segundo_numero:
#     print('son iguales')
#     if primer_numero < 20:
#         print('es menor a 20')
#     elif primer_numero < 30:
#         print('es menor a 30')
#     elif primer_numero < 40:
#         print('es menor a 40')
#     elif primer_numero < 50:
#         print('es menor a 50')
#     else:
#         print('no se cumplio ninguna condicion de las anteriores')
# else:
#     print('segundo_numero es menor que primer_numero')
    

# variable = 0
# if primer_numero < segundo_numero:
#     variable += 15
# elif primer_numero == segundo_numero:
#     variable += 24
#     if primer_numero < 20:
#         variable *= 15
#     elif primer_numero < 30:
#         variable /= 15
#     elif primer_numero < 40:
#         variable **= 15
#     elif primer_numero < 50:
#         variable -= 15
#     else:
#         print('no se cumplio ninguna condicion de las anteriores')
# else:
#     print('segundo_numero es menor que primer_numero')

# print(variable)

# =================================================================================================
# =================================================================================================

# Ej 1: Mayoría de edad (5min)
# Escribir un programa que le pregunte al usuario su edad y
# muestre por pantalla si es mayor de edad o no.

# edad = int(input('Ingrese su edad: '))

# print('Es menor de edad' if edad < 18 else 'Es mayor de edad')


# Ej 2: Marvel vs Capcom (20min)
# Un curso se ha dividido en dos grupos: A y B de acuerdo al nombre y a 
# una preferencia (Marvel o Capcom). 
# El grupo A está formado por fans de Marvel con un nombre anterior a la M y 
# los fans de Capcom con un nombre posterior a la N, y el grupo B por el resto. 
# Escribir un programa que pregunte al usuario su nombre y preferencia, 
# y muestre por pantalla el grupo que le corresponde.

# A >> (Marvel and nombre anterior M ) and Capcom and nombre posterior a N
# B >> lo que queda

# print('ESCRIBI TODO EN MINUSCULA!!!')
# nombre = input('Ingrese su nombre: ')
# preferencia = input('Ingrese su preferencia (capcom o marvel): ')

# if (preferencia == "marvel" and nombre < 'm' ) or (preferencia == "capcom" and nombre > 'n'):
#     print('Sos del grupo A!')
# else:
#     print('Sos del grupo B!')
    

# if preferencia == "marvel" and nombre < 'm':
#     print('Sos del grupo A!')
# elif preferencia == "capcom" and nombre > 'n':
#     print('Sos del grupo A!')
# else:
#     print('Sos del grupo B!')