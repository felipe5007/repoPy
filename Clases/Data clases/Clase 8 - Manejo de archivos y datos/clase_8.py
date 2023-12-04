# open, close (w, r, a)

# https://docs.python.org/3/library/functions.html#open




# open('C:\Users\cdbia\Desktop\47775\pepe\texto.txt')
# archivo = open('pepe/texto.txt', 'w')
# print(type(archivo))
# archivo.close()


# with open('prueba/texto.txt', 'w') as archivo:
#     print(type(archivo))
    

# with open('pepe/texto.txt', 'w') as archivo:
#     archivo.write('soy un texto nuevo')

# with open('pepe/texto.txt', 'w') as archivo:
#     archivo.write('soy otro texto\n')
#     # archivo.write(input('asd'))
#     archivo.write('ACA HAY MAS TEXTO')


# archivo = open('pepe/texto.txt', 'w')

# archivo.write('soy un texto nuevo')
# ...
# ...
# ...
# ...
# archivo.write('soy otro texto')
# archivo.write('ACA HAY MAS TEXTO')
# ...
# ...
# ...
# ...
# ...

# archivo.close()

# datos_persona = {
#     'nombre': input('Ingrese nombre:'),
#     'edad': int(input('Ingrese edad:')),
#     'apodo': input('Ingrese apodo:'),
# }

# with open('pepe/texto.txt', 'w') as archivo:
#     archivo.write(f'Nombre: {datos_persona["nombre"]} - Edad: {datos_persona["edad"]} - Apodo: {datos_persona["apodo"]}')


# with open('pepe/texto.txt', 'r') as archivo:
#     diccionario = archivo.read()
#     print(diccionario['nombre'])
    
    
# with open('pepe/texto.txt', 'w') as archivo:
#     archivo.write('soy un texto nuevo\n')
#     archivo.write('soy otro texto\n')
#     archivo.write('ACA HAY MAS TEXTO')



# with open('pepe/texto.txt', 'r') as archivo:
#     # print(archivo.read())
#     texto = archivo.read()
#     print(texto)
#     print('============================')
#     # print(archivo.read())
#     print(texto)
    
#     print('============================')
# print(texto)



# with open('pepe/texto.txt', 'r') as archivo:
#     print(archivo.readline())
#     print('============================')
#     print(archivo.readline())
#     print('============================')
#     print(archivo.readline())
#     print('============================')
#     print(archivo.readline())
#     print('============================')
#     print(archivo.readline())
#     print('============================')
#     print(archivo.readline())
#     print('============================')
#     print(archivo.readline())
#     print('============================')
#     print(archivo.readline())
#     print('============================')
#     print(archivo.readline())
#     print('============================')




# with open('pepe/texto.txt', 'r') as archivo:
#     print(archivo.readlines())
#     print('============================')
#     print(archivo.readlines())
#     print('============================')


# with open('pepe/texto.txt', 'w') as archivo:
#     archivo.write('á ñ')

# with open('pepe/texto.txt', 'r') as archivo:
#     print(archivo.read())
#     print('============================')
#     print(archivo.read())
#     print('============================')
#     archivo.seek(18)
#     print(archivo.readline())
#     print('============================')
#     archivo.seek(18)
#     print(archivo.readlines())
#     print('============================')



# JSON => js object notation

import json

# datos_persona = {
#     'nombre': 'Ricardo',
#     'edad': 45,
#     'apodo': 'Capitan',
# }

# # lista = [1,2,3,4,54,65,6,3]

# with open('mis_datos.json', 'w') as archivo:
#     # json.dump(2, archivo)
#     # json.dump(lista, archivo)
#     # json.dump(tuple(lista), archivo)
#     # json.dump(set(lista), archivo)
#     # json.dump('lista', archivo)
#     json.dump(datos_persona, archivo, indent=4)


# with open('mis_datos.json', 'r') as archivo:
#     mis_datos = json.load(archivo)
#     print(mis_datos['nombre'])
#     print(type(mis_datos))



