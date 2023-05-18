import pandas as pd
import numpy as np

matriz = pd.read_excel("matriz.xlsx")

letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
listafinal = np.vstack([matriz[letra].tolist() for letra in letras])

textoplano = 'RESULTADO PADRINO HIJO'
clave = 'GASKULURUK'



def encriptar (textoplano):
    mensajeencriptado = []
    for i in range (len(textoplano)):
    
        inidicecolumna = list(matriz["A"]).index(textoplano[i])
    
        indicerenglon = list(matriz["A"]).index(clave[i])
    
        letraencriptada = listafinal[inidicecolumna][indicerenglon]
        mensajeencriptado.append(letraencriptada)
    
    
    return mensajeencriptado


def desencriptar (mensajeencriptado): 
    mensajedesifrado = []
    for j in range (len(mensajeencriptado)):
        inidcecolumna = list(matriz["A"].tolist()).index(clave[j])
        indiceRenglon = list(listafinal[inidcecolumna]).index(mensajeencriptado[j])
        letratemp2 = listafinal[0][indiceRenglon]
        mensajedesifrado.append(letratemp2)
    return mensajedesifrado

def separarPalabra(parrafo): 
    arrayPalabras = parrafo.split()
    palabrasSeparadas = []
    textoEncriptado = []
    textoDesencriptado = []
    
    for i in range(len(arrayPalabras)):
        palabra = arrayPalabras[i]
        palabrasSeparadas.append(palabra)
    
    for x in range(len(palabrasSeparadas)): 
        palabraencriptada = encriptar(palabrasSeparadas[x])
        textoEncriptado.append(palabraencriptada)
        
    for j in range(len(textoEncriptado)): 
        palabraDesencriptada = desencriptar(textoEncriptado[j])
        textoDesencriptado.append(palabraDesencriptada)
    print("Palabras separadas: \n", palabrasSeparadas, "\nPalabras encriptadas: \n",textoEncriptado, "\nPalabras desencriptadas: \n" ,textoDesencriptado)
    return 1

separarPalabra(textoplano)
"""mensajeencriptado = encriptar(textoplano)
desencriptar(mensajeencriptado)"""