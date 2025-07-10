import pandas as pd
import matplotlib.pyplot as plt
import os

path = 'datos'
appointed_hours = pd.read_excel(os.path.join(path,'2025.xlsx'),index_col=None)
metadata = pd.DataFrame({})


print(appointed_hours['Estado cita'].unique())