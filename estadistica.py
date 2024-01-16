import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


variables=['Recepcionista','18_12_2023','5_01_2024','15_01_2024']

ventas_ingresadas = [['Alejandro', 564, 686, 753], 
                     ['Camila', 442, 601, 655], 
                     ['Betty', 1171, 1224, 1276], 
                     ['Felipe', 2757, 2764, 2771]]

venta_marginal= [['Alejandro', 0, 122, 67], 
                ['Camila', 0, 159, 54], 
                ['Betty', 0, 53, 52], 
                ['Felipe', 0, 7, 7]]

citas_creadas = [['Alejandro', 630, 784, 877], 
                ['Camila', 530, 739, 836], 
                ['Betty', 914, 979, 1044], 
                ['Felipe', 2778, 2789, 2799]]

cita_marginal =[['Alejandro', 0, 154, 93], 
                ['Camila', 0, 209, 97], 
                ['Betty', 0, 65, 65], 
                ['Felipe', 0, 65, 65]]

cambio_de_estado_de_citas=[['Alejandro', 1826, 2293, 2525], 
                           ['Camila', 1269, 1716, 1910], 
                           ['Betty', 3019, 3196, 3373], 
                           ['Felipe', 6672, 6688, 6704]]

cambio_marginal=[['Alejandro', 0, 467, 232], 
                ['Camila', 0, 447, 194], 
                ['Betty', 0, 177, 176], 
                ['Felipe', 0, 15, 16]]

df_ventas=pd.DataFrame(venta_marginal,columns=variables)
df_citas=pd.DataFrame(cita_marginal,columns=variables)
df_cambios=pd.DataFrame(cambio_marginal,columns=variables)


# Graficar datos de ventas
plt.figure(figsize=(10, 6))
for i in range(len(df_ventas)):
    plt.plot(df_ventas.columns[1:], df_ventas.iloc[i, 1:], marker='o', label=df_ventas['Recepcionista'][i])

plt.title('Ventas Ingresadas')
plt.xlabel('Fechas')
plt.ylabel('Ventas')
plt.legend()
plt.grid(True)
plt.show()

# Graficar datos de citas
plt.figure(figsize=(10, 6))
for i in range(len(df_citas)):
    plt.plot(df_citas.columns[1:], df_citas.iloc[i, 1:], marker='o', label=df_citas['Recepcionista'][i])

plt.title('Citas Creadas')
plt.xlabel('Fechas')
plt.ylabel('Citas')
plt.legend()
plt.grid(True)
plt.show()

# Graficar datos de cambios de estado de citas
plt.figure(figsize=(10, 6))
for i in range(len(df_cambios)):
    plt.plot(df_cambios.columns[1:], df_cambios.iloc[i, 1:], marker='o', label=df_cambios['Recepcionista'][i])

plt.title('Cambios de Estado de Citas')
plt.xlabel('Fechas')
plt.ylabel('Cambios de Estado')
plt.legend()
plt.grid(True)
plt.show()