import func_est as func
import pandas as pd
import os

path=os.path.join(os.getcwd(),"datos")

ventas_ingresadas:pd.DataFrame = func.lecturaDeExcels("ventas_ingresadas.xlsx",path)
citas_creadas:pd.DataFrame     = func.lecturaDeExcels("citas_creadas.xlsx",path)
cambio_estado:pd.DataFrame     = func.lecturaDeExcels("cambios_de_estado_de_cita.xlsx",path)
dias_trabajados:pd.DataFrame   = func.lecturaDeExcels("dias_trabajados.xlsx",path)


diff_ventas:pd.DataFrame = func.difference(ventas_ingresadas,dias_trabajados)
diff_citas:pd.DataFrame  = func.difference(citas_creadas,dias_trabajados)
diff_cambio:pd.DataFrame = func.difference(cambio_estado,dias_trabajados)

# Graficar datos de ventas
func.graphAll(diff_ventas,"Ventas diarias promedio",'Fechas', 'N° de ventas')

# Graficar Citas creadas por secretario
func.graphAll(diff_citas,"citas agendadas diariamente promedio",'Fechas', 'N° de citas')

# Gráfico de datos de cambio de estado de citas
func.graphAll(diff_cambio,"cambio de estado diario promedio",'Fechas','N° de cambios de estado')