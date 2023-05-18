# -*- coding: utf-8 -*-
"""
Created on Thu May 18 09:47:00 2023

@author: Olaf
"""
import pandas as pd
import numpy as np

matriz = pd.read_excel("matriz.xlsx")

letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
listafinal = np.vstack([matriz[letra].tolist() for letra in letras])

texto_plano = "ESTE ES UN TEXTO DE PRUEBA"
clave = "GASKULURUK"

mensaje_encriptado = []
for i, letra in enumerate(texto_plano):
    if letra in letras:
        indice_renglon = letras.index(clave[i % len(clave)])
        indice_columna = listafinal[:, indice_renglon].tolist().index(letra)
        letra_encriptada = letras[indice_columna]
        mensaje_encriptado.append(letra_encriptada)

print("Mensaje encriptado:", "".join(mensaje_encriptado))

mensaje_desencriptado = []
for i, letra in enumerate(mensaje_encriptado):
    indice_renglon = letras.index(clave[i % len(clave)])
    indice_columna = letras.index(letra)
    letra_desencriptada = listafinal[indice_columna][indice_renglon]
    mensaje_desencriptado.append(letra_desencriptada)

print("Mensaje desencriptado:", "".join(mensaje_desencriptado))


