import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Lee los datos procesados
df = pd.read_csv('datos_procesados.csv')

plt.figure(figsize=(10,6))
plt.hist(df['age'], bins=20, color='skyblue')
plt.title('Distribución de Edades')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.grid(axis='y', alpha=0.75)
plt.show()

# Obtener los valores para hombres y mujeres
valores_hombres = df[df['sex'] == True][['anaemia', 'diabetes', 'smoking', 'DEATH_EVENT']].sum().values
valores_mujeres = df[df['sex'] == False][['anaemia', 'diabetes', 'smoking', 'DEATH_EVENT']].sum().values

# Convertir los valores booleanos a números enteros
valores_hombres = [int(valor) for valor in valores_hombres]
valores_mujeres = [int(valor) for valor in valores_mujeres]

# Imprimir los valores de las variables
print(valores_hombres)
print(valores_mujeres)

# Configurar el gráfico de barras
etiquetas = ['Anemicos', 'Diabeticos', 'Fumadores', 'Muertos']
x = np.arange(len(etiquetas))
ancho = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
rectsTrue = ax.bar(x - ancho/2, valores_hombres, ancho, label='Hombres', color='blue')
rects2 = ax.bar(x + ancho/2, valores_mujeres, ancho, label='Mujeres', color='red')

# Agregar texto, etiquetas y título
ax.set_xlabel('Categorías')
ax.set_ylabel('Cantidad')
ax.set_title('Estadísticas de Salud por Género')
ax.set_xticks(x)
ax.set_xticklabels(etiquetas)
ax.legend()

plt.show()