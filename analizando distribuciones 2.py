import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Lee los datos procesados
df = pd.read_csv('datos_procesados.csv')

valores_anémicos = df['anaemia'].value_counts()
valores_diabéticos = df['diabetes'].value_counts()
valores_fumadores = df['smoking'].value_counts()
valores_muertos = df['DEATH_EVENT'].value_counts()

print("Valor de la anaemia: ", valores_anémicos)
print("Valor de la diabetes: ", valores_diabéticos)
print("Valor del fumar: ", valores_fumadores)
print("Valor de las muertes: ", valores_muertos)


anemicos = 'si','no' 
diabeticos =  'si','no' 
fumadores =  'si','no' 
muertos =  'si','no' 

# Crear las gráficas de torta
fig, axs = plt.subplots(1, 4)
axs[0].pie(valores_anémicos, labels=anemicos, autopct='%1.1f%%', startangle=90)
axs[1].pie(valores_diabéticos, labels=diabeticos, autopct='%1.1f%%', startangle=90)
axs[2].pie(valores_fumadores, labels=fumadores, autopct='%1.1f%%', startangle=90)
axs[3].pie(valores_muertos, labels=muertos, autopct='%1.1f%%', startangle=90)

# Ajustar los títulos de las gráficas
axs[0].set_title('Anemicos')
axs[1].set_title('Diabeticos')
axs[2].set_title('Fumadores')
axs[3].set_title('Muertos')

plt.show()