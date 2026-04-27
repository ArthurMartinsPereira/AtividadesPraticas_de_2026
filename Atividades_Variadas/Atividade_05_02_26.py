# Menu e funcionalidades para adicionar, mostrar e remover clientes da lista clientes.txt

class Cliente:
    def __init__(self, nome, idade, cpf, cidade):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.cidade = cidade

    def to_string(self):
        return f"{self.nome};{self.idade};{self.cpf};{self.cidade}\n"


def cadastro():
    nome = input("Nome: ")
    idade = input("Idade: ")
    cpf = input("CPF: ")
    cidade = input("Cidade: ")

    cliente = Cliente(nome, idade, cpf, cidade)
    with open("clientes.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(cliente.to_string())

    print("\nCliente cadastrado com sucesso!")


def mostrar_clientes():
    try:
        with open("clientes.txt", "r", encoding="utf-8") as arquivo:
            clientes = arquivo.readlines()
        if not clientes:
            print("\nNenhum cliente cadastrado...")
            return

        print("\n=== Clientes ===")
        for linha in clientes:
            nome, idade, cpf, cidade = linha.strip().split(";")
            print(f"Nome: {nome}|Idade: {idade}|CPF: {cpf}|Cidade: {cidade}")

    except FileNotFoundError:
        print("\nNenhum arquivo encontrado.")


def remover_cliente():
    cpf_remover = input("Escreva o CPF do cliente que deseja remover: ")

    try:
        with open("clientes.txt", "r", encoding="utf-8") as arquivo:
            clientes = arquivo.readlines()

        novos_clientes = []
        removido = False

        for linha in clientes:
            _, _, cpf, _ = linha.strip().split(";")
            if cpf != cpf_remover:
                novos_clientes.append(linha)
            else:
                removido = True

        with open("clientes.txt", "w", encoding="utf-8") as arquivo:
            arquivo.writelines(novos_clientes)

        if removido:
            print("\nCliente removido com sucesso!")
        else:
            print("\nCPF não encontrado.")

    except FileNotFoundError:
        print("\nNenhum arquivo encontrado.")


def menu():
    while True:
        print("\n=== Menu ===")
        print("1- Cadastrar Cliente")
        print("2- Mostrar Clientes")
        print("3- Remover Clientes")
        print("4- Sair")

        escolha = input("> ")

        if escolha == "1":
            cadastro()
        elif escolha == "2":
            mostrar_clientes()
        elif escolha == "3":
            remover_cliente()
        elif escolha == "4":
            print("Saindo...")
            break
        else:
            print("Opção Inválida!")


menu()
