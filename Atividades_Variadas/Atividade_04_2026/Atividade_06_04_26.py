def jogar():
    print("Pense em um número entre 1 e 100.")
    input("Precione ENTER quando estiver pronto...")

    baixo = 1
    alto = 100
    tentativas = 0

    while True:
        palpite = (baixo + alto) // 2
        tentativas += 1

        print(f"Meu palpite é {palpite}")
        resposta = input("É 'maior', 'menor' ou 'certo'?").lower()

        if resposta == "certo":
            print(f"Acertei em {tentativas} tentativas!")
            break
        elif resposta == "maior":
            baixo = palpite + 1
        elif resposta == "menor":
            alto = palpite - 1
        else:
            print("Resposta Inválida!")


if __name__ == "__main__":
    jogar()
