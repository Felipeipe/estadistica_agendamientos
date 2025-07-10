import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def lecturaDeExcels(name:str,ruta:str)->pd.DataFrame:
    """Lee un excel de una ruta en especifico, de un nombre 'name'
    """
    return pd.read_excel(os.path.join(ruta,name),index_col=None)

