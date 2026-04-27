# Menu dos diferentes gráficos dos dados dos clientes.

import pandas as pd
import matplotlib.pyplot as plt


def carregar_dados():
    return pd.read_csv("clientes.txt", sep=";", names=["nome", "idade", "cpf", "cidade"])


# Gráfico de Distribuição de Idades:
def graf_01():
    df = carregar_dados()
    plt.figure()
    df["idade"].hist(bins=10)

    plt.title("Distribuição de Idades dos Clientes")
    plt.xlabel("Idade")
    plt.ylabel("Quantidade")
    print("\nIdade Média", df["idade"].mean())
    print("Idade Mínima:", df["idade"].min())
    print("Idade Máxima:", df["idade"].max())

    plt.tight_layout()
    plt.show()


# Gráfico de Clientes por Cidade:
def graf_02():
    df = carregar_dados()
    clientes_cidade = df["cidade"].value_counts()

    plt.figure()
    clientes_cidade.sort_values().plot(kind="bar")

    plt.title("Clientes por Cidade")
    plt.xlabel("Cidade")
    plt.ylabel("Quantidade")

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Gráfico de Idade Média por Cidade
def graf_03():
    df = carregar_dados()
    media_idade = df.groupby("cidade")["idade"].mean()

    plt.figure()
    media_idade.plot(kind="bar")

    plt.title("Idade Média por Cidade")
    plt.ylabel("Idade Média")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Gráfico de Distribuição por Grupo de Idade
def graf_04():
    df = carregar_dados()

    def classificar_idade(idade):
        if idade < 25:
            return "Jovem:"
        elif idade < 40:
            return "Adulto:"
        else:
            return "Sênior:"

    df["grupo_idade"] = df["idade"].apply(classificar_idade)
    print(df["grupo_idade"].value_counts())

    plt.figure()
    df["grupo_idade"].value_counts().plot(kind="pie", autopct="%1.1f%%")

    plt.title("Distribuição por Grupo Idade")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()


def menu():
    while True:
        print("=== Menu de Gráficos ===")
        print("1- Distribuição de Idades")
        print("2- Número de Clientes por Cidade")
        print("3- Idade Média por Cidade")
        print("4- Distribuição por Grupo Idade")
        print("5- Sair")

        escolha = input(">")

        if escolha == "1":
            graf_01()
        elif escolha == "2":
            graf_02()
        elif escolha == "3":
            graf_03()
        elif escolha == "4":
            graf_04()
        elif escolha == "5":
            break
        else:
            print("Opção Inválida!")


menu()
