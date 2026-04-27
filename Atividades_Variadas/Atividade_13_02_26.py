# Menu de busca parcial dos clientes (buscar por nome, idade, cidade)

def menu_busca():
    while True:
        print("\n=== Buscar Clientes ===")
        print("1- Busca por Nome")
        print("2- Busca por Cidade")
        print("3- Busca por Faixa de Idade")
        print("4- Sair")

        escolha = input(">")

        if escolha == "1":
            busca_nome()
        elif escolha == "2":
            busca_cidade()
        elif escolha == "3":
            busca_idade()
        elif escolha == "4":
            break
        else:
            print("Opção Inválida!")


def carregar_clientes():
    try:
        with open("clientes.txt", "r", encoding="utf8") as arquivo:
            linhas = arquivo.readlines()

        clientes = []

        for linha in linhas:
            nome, idade, cpf, cidade = linha.strip().split(";")

            clientes.append({
                "nome": nome,
                "idade": int(idade),
                "cpf": cpf,
                "cidade": cidade
            })

        return clientes

    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return []


def busca_nome():
    clientes = carregar_clientes()
    termo = input("Digite o nome ou parte do nome: ").lower()
    encontrados = []

    for cliente in clientes:
        if termo in cliente["nome"].lower():
            encontrados.append(cliente)

    mostrar_resultados(encontrados)


def busca_cidade():
    clientes = carregar_clientes()
    busc_cid = input("Digite a Cidade: ").lower()
    encontrados = []

    for cliente in clientes:
        if cliente["cidade"].lower() == busc_cid:
            encontrados.append(cliente)

    mostrar_resultados(encontrados)


def busca_idade():
    clientes = carregar_clientes()
    try:
        idade_min = int(input("Idade mínima: "))
        idade_max = int(input("Idade máxima: "))
    except ValueError:
        print("Digite números válidos!")
        return

    encontrados = []

    for cliente in clientes:
        if idade_min <= cliente["idade"] <= idade_max:
            encontrados.append(cliente)

    mostrar_resultados(encontrados)


def mostrar_resultados(lista):
    if not lista:
        print("Nenhum cliente encontrado.")
        return

    print("\n === Resultados ===")
    for clientes in lista:
        print(f"Nome: {clientes['nome']} | "
              f"Idade: {clientes['idade']} | "
              f"CPF: {clientes['cpf']} | "
              f"Cidade: {clientes['cidade']}")


menu_busca()
