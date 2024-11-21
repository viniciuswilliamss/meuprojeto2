class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.projetos = []

    def adicionar_projeto(self, projeto):
        self.projetos.append(projeto)

    def listar_projetos(self):
        return [projeto.nome for projeto in self.projetos]

class Projeto:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

class GerenciadorClientes:
    def __init__(self):
        self.clientes = {}

    def adicionar_cliente(self, cliente):
        self.clientes[cliente.email] = cliente

    def listar_clientes(self):
        return [cliente.nome for cliente in self.clientes.values()]

    def encontrar_cliente(self, email):
        return self.clientes.get(email)

def main():
    gerenciador = GerenciadorClientes()

    while True:
        print("\n1. Adicionar Cliente")
        print("2. Adicionar Projeto a Cliente")
        print("3. Listar Clientes")
        print("4. Listar Projetos de um Cliente")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do Cliente: ")
            email = input("Email do Cliente: ")
            cliente = Cliente(nome, email)
            gerenciador.adicionar_cliente(cliente)
            print(f"Cliente {nome} adicionado com sucesso!")

        elif opcao == '2':
            email = input("Email do Cliente: ")
            cliente = gerenciador.encontrar_cliente(email)
            if cliente:
                nome_projeto = input("Nome do Projeto: ")
                descricao_projeto = input("Descrição do Projeto: ")
                projeto = Projeto(nome_projeto, descricao_projeto)
                cliente.adicionar_projeto(projeto)
                print(f"Projeto {nome_projeto} adicionado ao cliente {cliente.nome}.")
            else:
                print("Cliente não encontrado.")

        elif opcao == '3':
            clientes = gerenciador.listar_clientes()
            print("Clientes:")
            for c in clientes:
                print(c)

        elif opcao == '4':
            email = input("Email do Cliente: ")
            cliente = gerenciador.encontrar_cliente(email)
            if cliente:
                projetos = cliente.listar_projetos()
                print(f"Projetos de {cliente.nome}: {projetos}")
            else:
                print("Cliente não encontrado.")

        elif opcao == '5':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
