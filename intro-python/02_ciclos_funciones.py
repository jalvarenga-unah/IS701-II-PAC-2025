# -*- coding: utf-8 -*-
"""02-ciclos-funciones

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bBd76BiBMACFXgmHq8sUN8tPwA4g0j4C
"""

rango = range(1, 11, 2)

postres = ["galletas", "cheescake", "pie"]

# print(list(rango))
for i in postres:
  print(i)

mascota = {
    'nombre': 'Apolo',
    'raza': 'Terrier',
    'vacuna':{
            'nombre': 'Vacuna 1',
            'fecha': '2022-01-01'
        }
}

# for key in mascota:
#   print(mascota[key])

for key, value in mascota.items():
  print( value)

while True:
  print('hola')
  break

"""# Funciones / metodos"""

# Todas las funciones retornan: None, a menos que indique lo contrario
def saludo():
  print('Hola mundo desde una funcion')
  # return 'Hola'

# saludo = 'Hola' # ❌ reemplaza el valor de la refenrecia en memoria, por una cadena

result = saludo() # None

result = 'Hola' # no afecta en la ejecución de la función

print(result)

def saludo2() -> str:
  print("esta es una nueva funcion")
  return True

print(saludo2())

def multi(a:int, b: int) -> int:

  if not isinstance(a, (int,float)):
    print('a no es un numero')
    return

  # if not isinstance(b, (int,float)):
  #   print('b no es un numero')
  #   return

  if not type(b) == int and not type(b) == float :
    print('b no es un numero')
    return

  return a * b

print((multi(2, 2.3)))

def div(a,b):

  try:
    result = a / b
  except:
    print('asegurese de enviar los datos correctos')
    return

  return result

div(4,2)

def suma( *nums ):

  print(nums)
  return sum(nums)

suma(1,2,3,4,3,2,1)

def saludar( **kargs ):
  print(kargs['nombre'])

saludar(nombre="Juan", edad=31, apellido='Alvarenga')

help(saludar)

import math as Math

def calcArea(**args):

  '''
  esta funcion calcula el area de un circulo o un cuadrado
  :param args:
    tipo: str puede ser, circulo o cuadrado
    radio: int o float
    base: int o float
    altura: int o float
  :return:
  '''

  area = None

  if args['tipo'] == 'circulo':
    area = Math.pi * args['radio'] ** 2
  elif args['tipo'] == 'cuadrado':
    area = args['base'] * args['altura']
  else:
    print('no es una figura valida')

  return area

help(calcArea)

calcArea(tipo='cuadrado', base = 4, altura = 3)