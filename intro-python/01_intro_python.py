# -*- coding: utf-8 -*-
"""01-Intro-python

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qnlDMCUzKggGUx01vtexM4Hg1SMEa65w

## Caracteristicas de pyhton

- Es un lenguaje no tipado
- Es Identado (las tabulaciones importan)
- No termina con ;
- Lenguaje multi-paradigma
- Multi-plataforma
- Orientado al analisis de datos
"""

# Declaración de variables
nombre = "Juan" # una variable "nombre" -> Juan
edad = 31
altura : float = 1.60
esMayor = edad > 18

print((altura))
print(type(altura))

print("Hola mundo")
nombre = "Enrique"
print(nombre)
print(type(nombre))
print(type(edad))

print(type(esMayor))

numero = "3"
print(type(numero))
numero = int(numero)
numero = True
print(type(numero))

print( "Hola me llamo " + nombre + " tengo  "+ str(edad) + " años" )
print(f"Hola me llamo {nombre} tengo {edad} años")

"""## Condiciones"""

if edad < 18:
  print("es mayor de edad")
  print("está dentro de la condición verdadera")
elif edad == 18:
  print("es un adulto")
else: #linter
  print("es menor de edad")
print("fuera del IF")

cadena = "HolA mundo" # -> objetos iterables

nulo = None

if "a" in cadena or "A" in cadena:
  print("está en la cadena")
else:
  print("no está en la cadena")

"""## Estructuras (listas, diccionarios y tuplas)"""

#Listas

numeros = [1, 2, 3,"Juan", 4, 5, True, "Hola"]
copia = numeros.copy()
copia2 = tuple(numeros) # convertir una lista a una tupla


print(copia2)

numeros.append('Mundo')
numeros.insert(2, 'Juan')

print(numeros.count("Juan")) # cuenta las veces en que aparece en la lista

numeros.remove('Juan') # Elimina la primer coicidencia del valor buscado

print(numeros)
print(len(numeros)) # retorna el tamaño de la lista
print((copia)) # retorna el tamaño de la lista
print(copia2)
# copia = numeros.copy() # Reliza una copia integra del obejto

#Tuplas: es una lista inmutable, se queda tal cual fue inicialziada
tupla = ( 'Hola', 'Mundo' )

print(tupla)
print(tupla.index('Hola'))

# Diccionario

# clave -> valor
mascota = {
    'nombre': 'Apolo',
    'raza': 'Terrier',
    'vacuna':{
            'nombre': 'Vacuna 1',
            'fecha': '2022-01-01'
        }
}

mascota2 = dict(
  nombre='Polar'
)


mascota['edad'] = 2

# mascota.popitem() # elimina el ultimo elemento
# mascota.pop('raza') # elimina la clave y el valor

print(mascota.keys())
print(mascota.values())
print(mascota.items())
print(mascota2)
print('+++++++++++')
print(mascota['vacuna'].keys())
print(mascota['vacuna'].values())
print(mascota['vacuna'].items())