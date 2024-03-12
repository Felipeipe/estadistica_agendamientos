import func_est as func
import pandas as pd
import os

if __name__=='__main__':
    
    path:str =os.path.join(os.getcwd(),"datos")

    #Lectura de excels y conversion a formato pd.DataFrame
    ventas_ingresadas:pd.DataFrame = func.lecturaDeExcels("ventas_ingresadas.xlsx",path)
    citas_creadas:pd.DataFrame     = func.lecturaDeExcels("citas_creadas.xlsx",path)
    cambio_estado:pd.DataFrame     = func.lecturaDeExcels("cambios_de_estado_de_cita.xlsx",path)
    dias_trabajados:pd.DataFrame   = func.lecturaDeExcels("dias_trabajados.xlsx",path)

    #creacion de DataFrames que necesitamos graficar
    diff_ventas:pd.DataFrame = func.generador_promedio(func.difference(ventas_ingresadas,dias_trabajados))
    diff_citas:pd.DataFrame  = func.generador_promedio(func.difference(citas_creadas,dias_trabajados))
    diff_cambio:pd.DataFrame = func.generador_promedio(func.difference(cambio_estado,dias_trabajados))

    func.graph(diff_ventas,"Citas agendadas","Velocidad de agendamiento diario")