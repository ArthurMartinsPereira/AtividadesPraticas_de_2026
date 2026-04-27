# Machine Learning simples com o K-Means Clustering

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv("clientes.txt", sep=";", names=["nome", "idade", "cpf", "cidade"])
print(df.head())
print("--------------------------------------")


def Clustering():
    df_ml = df.copy()
    df_ml["cidade_cod"] = df_ml["cidade"].astype("category").cat.codes
    dados = df_ml[["idade", "cidade_cod"]]

    kmeans = KMeans(n_clusters=3, random_state=42)
    df_ml["cluster"] = kmeans.fit_predict(dados)
    print(df_ml[["nome", "idade", "cidade", "cluster"]].head(20))

    plt.figure()
    plt.scatter(
        df_ml["idade"],
        df_ml["cidade_cod"],
        c=df_ml["cluster"]
    )

    plt.xlabel("idade")
    plt.ylabel("Cidade (codificada)")
    plt.title("Cluster de Clientes (K-Means")
    plt.show()


Clustering()
