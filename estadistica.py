import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


ventas_ingresadas=pd.read_excel("ventas_ingresadas.xlsx",index_col=None)
citas_creadas=pd.read_excel("citas_creadas.xlsx",index_col=None)
cambio_estado=pd.read_excel("cambios_de_estado_de_cita.xlsx",index_col=None)
dias_trabajados=pd.read_excel("dias_trabajados.xlsx",index_col=None)




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

diff_ventas=difference(ventas_ingresadas,dias_trabajados)
diff_citas=difference(citas_creadas,dias_trabajados)
diff_cambio=difference(cambio_estado,dias_trabajados)


# Graficar datos de ventas
plt.figure(figsize=(10, 6))
for i in range(len(diff_ventas)):
    plt.plot(diff_ventas.columns[1:], diff_ventas.iloc[i, 1:], marker='o', label=diff_ventas['Recepcionista'][i])

plt.title('Ventas Ingresadas')
plt.xlabel('Fechas')
plt.ylabel('Ventas diarias en promedio')
plt.legend()
plt.grid(True)
plt.show()

# Graficar datos de citas
plt.figure(figsize=(10, 6))
for i in range(len(diff_citas)):
    plt.plot(diff_citas.columns[1:], diff_citas.iloc[i, 1:], marker='o', label=diff_citas['Recepcionista'][i])

plt.title('Citas Creadas')
plt.xlabel('Fechas')
plt.ylabel('Agendamiento diario promedio')
plt.legend()
plt.grid(True)
plt.show()

# Graficar datos de cambios de estado de citas
plt.figure(figsize=(10, 6))
for i in range(len(diff_cambio)):
    plt.plot(diff_cambio.columns[1:], diff_cambio.iloc[i, 1:], marker='o', label=diff_cambio['Recepcionista'][i])

plt.title('Cambios de Estado de Citas')
plt.xlabel('Fechas')
plt.ylabel('Cambios de Estado')
plt.legend()
plt.grid(True)
plt.show()

