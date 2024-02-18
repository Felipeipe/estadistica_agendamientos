import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

path=os.path.join(os.getcwd(),"datos")


ventas_ingresadas:pd.DataFrame = pd.read_excel(os.path.join(path,"ventas_ingresadas.xlsx"),index_col=None)
citas_creadas:pd.DataFrame     = pd.read_excel(os.path.join(path,"citas_creadas.xlsx"),index_col=None)
cambio_estado:pd.DataFrame     = pd.read_excel(os.path.join(path,"cambios_de_estado_de_cita.xlsx"),index_col=None)
dias_trabajados:pd.DataFrame   = pd.read_excel(os.path.join(path,"dias_trabajados.xlsx"),index_col=None)




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

def graph(df:pd.DataFrame, titulo:str, xlabel:str, ylabel:str) -> None:
    """Graficador de recepcionistas
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


diff_ventas:pd.DataFrame = difference(ventas_ingresadas,dias_trabajados)
diff_citas:pd.DataFrame  = difference(citas_creadas,dias_trabajados)
diff_cambio:pd.DataFrame = difference(cambio_estado,dias_trabajados)

# Graficar datos de ventas
graph(diff_ventas,"Ventas diarias promedio",'Fechas', 'N° de ventas')

# Graficar Citas creadas por secretario
graph(diff_citas,"citas agendadas diariamente promedio",'Fechas', 'N° de citas')

# Gráfico de datos de cambio de estado de citas
graph(diff_cambio,"cambio de estado diario promedio",'Fechas','N° de cambios de estado')