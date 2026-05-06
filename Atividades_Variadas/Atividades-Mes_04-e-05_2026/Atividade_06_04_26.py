import json
import os
import random


def carregar_dados():
    if os.path.exists("dados.json"):
        with open("dados.json", "r") as f:
            dados = json.load(f)
            return {int(k): v for k, v in dados.items()}
    else:
        return {i: 1 for i in range(1, 101)}


frequencia = carregar_dados()


def salvar_dados(frequencia):
    with open("dados.json", "w") as f:
        json.dump(frequencia, f)


def jogar():
    print("Pense em um número entre 1 e 100.")
    input("Precione ENTER quando estiver pronto...")

    baixo = 1
    alto = 100
    tentativas = 0

    while True:
        possiveis = {k: v for k, v in frequencia.items() if baixo <= k <= alto}

        if random.random() < 0.5:
            palpite = (baixo + alto) // 2
        else:
            palpite = max(possiveis, key=possiveis.get)

        tentativas += 1

        print(f"Meu palpite é {palpite}")
        resposta = input("É 'maior', 'menor' ou 'certo'?").lower()

        if resposta == "certo":
            print(f"Acertei em {tentativas} tentativas!")
            frequencia[palpite] += 1
            salvar_dados(frequencia)
            break
        elif resposta == "maior":
            baixo = palpite + 1
        elif resposta == "menor":
            alto = palpite - 1
        else:
            print("Resposta Inválida!")

        if baixo > alto:
            print("Hmm... suas respostas foram inconsistentes 😅")
            break

    print("Top 5 números mais escolhidos:")
    top = sorted(frequencia.items(), key=lambda x: x[1], reverse=True)[:5]
    for num, freq in top:
        print(f"{num}: {freq}")


if __name__ == "__main__":
    while True:
        jogar()
        continuar = input("Jogar novamente? (s/n): ").lower()
        if continuar != "s":
            break
