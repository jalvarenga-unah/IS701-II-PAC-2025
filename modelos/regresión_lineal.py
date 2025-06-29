# -*- coding: utf-8 -*-
"""Regresión Lineal

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YViDUOkuJ2TaFQJfz8sC-bBOw9HS47Ig
"""

# c -> F = c * (9/5) + 32

#Conjunto de datos que me sirve como expericia pasada

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * (9/5) + 32
    return fahrenheit

c = [ -40, -20, 0 -8, 15, 22, 36, 48 ] # caracteristicas
f = []
for value in c:
    f.append(celsius_to_fahrenheit(value))

import pandas as pd

data = pd.DataFrame({
    'celsius': c,
    'fahrenheit': f
})

data

X = data['celsius']
y = data['fahrenheit']

# [-40. ,  -4. ,  17.6,  59. ,  71.6,  96.8, 118.4]
# [ [-40. ] ,  [-4]. ,  [17.6],  59. ,  71.6,  96.8, 118.4]

X_procesada = X.values.reshape(-1, 1)
y_procesada = y.values.reshape(-1, 1)

from sklearn.linear_model import LinearRegression

modelo = LinearRegression()

#Entrenamiento

modelo.fit(X_procesada, y_procesada)

modelo.predict([[100]])

modelo.score(X_procesada, y_procesada)

print(modelo.coef_) # peso
print(modelo.intercept_) # bias