# Utilizando o Método do Cotovelo(Elbow Method)

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# Leitura dos dados:
df = pd.read_csv("clientes.txt", sep=";",
                 names=["nome", "idade", "cpf", "cidade"])
df_ml = df.copy()

# Pré-processamento dos dados:
df_cidades = pd.get_dummies(df_ml["cidade"], drop_first=True)

dados = pd.concat([df_ml[["idade"]], df_cidades], axis=1)

# Escalonamento:
scaler = StandardScaler()
dados_escalados = scaler.fit_transform(dados)

# Método do Cotovelo:
inercia = []
k_range = range(1, 11)
for k in k_range:
    modelo = KMeans(n_clusters=k, random_state=42, n_init=10)
    modelo.fit(dados_escalados)
    inercia.append(modelo.inertia_)

plt.figure(figsize=(6, 4))
plt.plot(k_range, inercia, marker="o")
plt.title("Elbow Method - Número Ideal de Clusters")
plt.xlabel("Número de Clusters")
plt.ylabel("Inércia")
plt.grid(True)
plt.show()


# Nomeação dos Clusters:
def nome_cluster(idade_media):
    if idade_media < 27:
        return "Jovems"
    elif idade_media < 40:
        return "Adultos"
    else:
        return "Sêniores"


# KMeans Final e PCA para Visualização:
kmeans = KMeans(n_clusters=4, random_state=42)
df_ml["cluster"] = kmeans.fit_predict(dados_escalados)

pca = PCA(n_components=2)
dados_2d = pca.fit_transform(dados_escalados)

resumo = df_ml.groupby("cluster")["idade"].mean()
for cluster, idade_media in resumo.items():
    print(f"Cluster {cluster}: {nome_cluster(idade_media)}")


# Plot PCA:
plt.figure(figsize=(6, 5))
plt.scatter(
    dados_2d[:, 0],
    dados_2d[:, 1],
    c=df_ml["cluster"],
    cmap="viridis"
)

plt.title("Clusters de Clientes(PCA)")
plt.xlabel("Componente Principal 1")
plt.ylabel("Componente Principal 2")
plt.colorbar(label="Cluster")
plt.show()

# Resumos:
print("\nResumo por Cluster: ")
print(df_ml.groupby("cluster")[["idade"]].mean())

print("\nQuantidade por Cluster: ")
print(df_ml["cluster"].value_counts())

print("\nPerfil dos Clusters:")
for cluster_id in sorted(df_ml["cluster"].unique()):
    grupo = df_ml[df_ml["cluster"] == cluster_id]

    print(f"Cluster {cluster_id}")
    print("Idade Média: ", round(grupo["idade"].mean(), 1))
    print("Quantidade: ", len(grupo))
    print("Cidade mais Comum:", grupo["cidade"].value_counts().idxmax())
    print("-" * 30)
