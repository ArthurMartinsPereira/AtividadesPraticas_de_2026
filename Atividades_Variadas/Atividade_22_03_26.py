from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
import itertools
import seaborn as sns

# Carregar Dataset e Gerar o Primeiro Gráfico:
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

df["target"] = iris.target
print(df.head())


def iris():
    df.hist(figsize=(10, 8))
    plt.tight_layout()
    plt.show()


# Scatter plot:
def scatter():
    colunas = df.columns[:-1]

    for x, y in itertools.combinations(colunas, 2):
        plt.figure()
        plt.scatter(df[x], df[y], c=df["target"])
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(f"{x} vs {y}")
        plt.show()


# Heatmap para correção:
def heatmap():
    plt.figure(figsize=(8, 6))
    sns.heatmap(df.corr(), annot=True)
    plt.show()


def menu():
    print("=== Menu ===")
    print("1- Gráfico Inicial")
    print("2- Scatter Plot")
    print("3- Heatmap")
    print("4- Sair")

    while True:
        escolha = input("Escolha uma das opções(1 a 4): ")

        if escolha == "1":
            iris()
        elif escolha == "2":
            scatter()
        elif escolha == "3":
            heatmap()
        elif escolha == "4":
            print("Saindo...")
            break
        else:
            print("Opção Inválida!")


menu()
