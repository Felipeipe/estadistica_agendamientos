import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def lecturaDeExcels(name:str,ruta:str)->pd.DataFrame:
    """Lee un excel de una ruta en especifico, de un nombre 'name'
    """
    df=pd.read_excel(os.path.join(ruta,f"{name}"),index_col=None)
    return df

def difference(df:pd.DataFrame,dt:pd.DataFrame) -> pd.DataFrame:
    """
    Calcula la variación promedio entre dos columnas, ponderados por un DataFrame 
    """
    j=2
    df0=df.copy()
    df0[df0.columns[1]]=np.zeros(len(df0))
    while j < len(df.columns):
        df0[df0.columns[j]]=(df[df.columns[j]]-df[df.columns[j-1]])/dt[dt.columns[j]]
        j+=1
    return df0

"""
def graph(df:pd.DataFrame, recepcionista:str, titulo:str, xlabel:str, ylabel:str) -> None:
    plt.figure(figsize=(10, 6))
    plt.plot(df.columns[1:], df.loc[f"{recepcionista}", 1:], marker='o', label=f"{recepcionista}")
    plt.plot(df.columns[1:], df.loc["Promedio", 1:], marker='o', label="Promedio")
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()
    pass
"""
def graphAll(df:pd.DataFrame, titulo:str, xlabel:str, ylabel:str)->None:
    """ Grafica los datos del DataFrame 'df' dentro de todos los 
    
    """
    plt.figure(figsize=(10, 6))
    for i in range(len(df)):
        plt.plot(df.columns[1:], df.iloc[i, 1:], marker='o', label=df['Recepcionista'][i])

    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()
    pass


def promedio(df:pd.DataFrame,index:int)->float:
    """
    calcula el promedio de una columna de los DataFrame que
    se están trabajando
    """
    if index<1:
        raise IndexError("indice debe ser mayor o igual que 1")
    suma=sum(df[df.columns[index]])
    n=len(df[df.columns[index]])
    prom=suma/n
    return prom

def generador_promedio(df:pd.DataFrame)->pd.DataFrame:
    df0=df.copy()
    D={}
    for i,key in enumerate(df.columns.to_list()):
        if key=="Recepcionista":
            D[key]="Promedio"
            continue
        D[key]=promedio(df0,i)
    # Crear una nueva fila con los valores calculados
    nueva_fila = pd.DataFrame(D, index=[len(df)])  # Usando la longitud del DataFrame como índice
    # Concatenar el DataFrame original con la nueva fila
    df0 = pd.concat([df0, nueva_fila])
    return df0


