import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


ventas_ingresadas=pd.read_excel("ventas_ingresadas.xlsx",index_col=None)
citas_creadas=pd.read_excel("citas_creadas.xlsx",index_col=None)
cambio_estado=pd.read_excel("cambios_de_estado_de_cita.xlsx",index_col=None)
dias_trabajados=pd.read_excel("dias_trabajados.xlsx",index_col=None)



diff_ventas=ventas_ingresadas.copy()
diff_citas=citas_creadas.copy()
diff_cambio=cambio_estado.copy()



i=2
diff_ventas[diff_ventas.columns[1]]=np.zeros(len(diff_ventas))
while i<len(ventas_ingresadas.columns):
    diff_ventas[diff_ventas.columns[i]]=(ventas_ingresadas[ventas_ingresadas.columns[i]]-ventas_ingresadas[ventas_ingresadas.columns[i-1]])*1/dias_trabajados[dias_trabajados.columns[i]]
    i+=1

i=2
diff_citas[diff_citas.columns[1]]=np.zeros(len(diff_citas))
while i<len(citas_creadas.columns):
    diff_citas[diff_citas.columns[i]]=(citas_creadas[citas_creadas.columns[i]]-citas_creadas[citas_creadas.columns[i-1]])*1/dias_trabajados[dias_trabajados.columns[i]]
    i+=1

i=2
diff_cambio[diff_cambio.columns[1]]=np.zeros(len(diff_cambio))
while i<len(cambio_estado.columns):
    diff_cambio[diff_cambio.columns[i]]=(cambio_estado[cambio_estado.columns[i]]-cambio_estado[cambio_estado.columns[i-1]])*1/dias_trabajados[dias_trabajados.columns[i]]
    i+=1



# Graficar datos de ventas
plt.figure(figsize=(10, 6))
for i in range(len(diff_ventas)):
    plt.plot(diff_ventas.columns[1:], diff_ventas.iloc[i, 1:], marker='o', label=diff_ventas['Recepcionista'][i])

plt.title('Ventas Ingresadas')
plt.xlabel('Fechas')
plt.ylabel('Ventas')
plt.legend()
plt.grid(True)
plt.show()

# Graficar datos de citas
plt.figure(figsize=(10, 6))
for i in range(len(diff_citas)):
    plt.plot(diff_citas.columns[1:], diff_citas.iloc[i, 1:], marker='o', label=diff_citas['Recepcionista'][i])

plt.title('Citas Creadas')
plt.xlabel('Fechas')
plt.ylabel('Citas')
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

