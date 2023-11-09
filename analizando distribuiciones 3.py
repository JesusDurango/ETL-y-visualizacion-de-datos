import plotly.graph_objects as go
import numpy as np
import pandas as pd
from sklearn.manifold import TSNE
import plotly.express as px

df = pd.read_csv("datos_procesados.csv")

dfnew = df.drop(columns=["DEATH_EVENT", "categoria_edad"])

X = dfnew.values

np.savetxt("X.csv", X, delimiter=",")

y = df["DEATH_EVENT"]

y = y.ravel()

np.savetxt("y.csv", y, delimiter=",")

X_embedded = TSNE(
    n_components=3,
    learning_rate='auto',
    init='random',
    perplexity=3
).fit_transform(X)

y1 =df["DEATH_EVENT"].replace({1: "Fallecido", 0: "vivo"})
print(y1)

fig = px.scatter_3d(
    x=X_embedded[:, 0],
    y=X_embedded[:, 1],
    z=X_embedded[:, 2],
    color=y1,
    color_continuous_scale='inferno',
    opacity=0.8,
)

fig.show()

