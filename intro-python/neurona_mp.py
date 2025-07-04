# -*- coding: utf-8 -*-
"""Neurona MP

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EPtUnNuSMWPuB2sOJKug1EZh5XllInwo
"""

from sklearn.metrics import accuracy_score

class MPNeuron:

  def __init__(self, t):
    self.threshold = t

  def model(self, X:list): # [1,1,0,0]
    if self.threshold is None:
      print("El trheshold debe ser mayor a cero")
    else:
      return sum(X) >= self.threshold

  def predict(self, X): # [[1,0,0,1,0,1,1,0,1,0],[1,0,0,1,0,1,1,0,1,0],[1,0,0,1,0,1,1,0,1,0]]
    predicciones = []

    for x in X:
      predicciones.append(self.model(x))

    return predicciones


  def fit(self, X, y):

    prom = {}

    for t in range(X.shape[1] + 1):
      self.threshold = t # 0,1,2,3....30
      y_pred = self.predict(X) # -> 0 ó 1

      prom[t] = accuracy_score(y, y_pred)

    return max(prom, key=prom.get) # el threshold mas optimo

neuron = MPNeuron(t=3)

# si voy a la playa o no
respuestas = [1, 0, 0, 1]

# [[1,1,0,0],[1,1,0,0],[1,1,0,0],[1,1,0,0]]

pred = neuron.model(respuestas)

pred

from sklearn.datasets import load_breast_cancer
import pandas as pd
import numpy as np

data = load_breast_cancer()

data.data

df_cancer = pd.DataFrame(data.data, columns = data.feature_names)

df_cancer.shape

df_cancer

#separar los datos en 2 conjuntos: entrenamiento y pruebas

from sklearn.model_selection import train_test_split

X = df_cancer
y = data.target


#  random_state=42 => evita que se mezclen los registros antes de hacer el split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,)

y_test

X_train_bin = X_train.apply(pd.cut, bins=2, labels=[1,0])
X_test_bin = X_test.apply(pd.cut, bins=2, labels=[1,0])

X_train_bin.to_numpy()

# obtener el threshold optimo
neuron = MPNeuron(t=None)

threshold = neuron.fit( X_train_bin.to_numpy(), y_train )

threshold

predicciones = neuron.predict(X_test_bin.to_numpy())

result = accuracy_score(predicciones, y_test)

result

from sklearn.metrics import confusion_matrix

confusion_matrix(y_test, predicciones)