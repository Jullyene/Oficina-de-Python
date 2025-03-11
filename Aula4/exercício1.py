def exibir_menu():
    print("\nMENU - AGENDA DE CONTATOS")
    print("1. Adicionar Contato")
    print("2. Buscar Contato")
    print("3. Editar Contato")
    print("4. Remover Contato")
    print("5. Exibir Todos os Contatos")
    print("6. Sair")

def adicionar_contato(agenda):
    nome = input("Digite o nome do contato: ").strip()
    if nome in agenda:
        print("Contato já existe!")
        return
    telefone = input("Digite o telefone: ").strip()
    email = input("Digite o e-mail: ").strip()
    agenda[nome] = [telefone, email]
    print("Contato adicionado com sucesso!")

def buscar_contato(agenda):
    nome = input("Digite o nome do contato: ").strip()
    if nome in agenda:
        print(f"Nome: {nome} | Telefone: {agenda[nome][0]} | E-mail: {agenda[nome][1]}")
    else:
        print("Contato não encontrado!")

def editar_contato(agenda):
    nome = input("Digite o nome do contato a ser editado: ").strip()
    if nome in agenda:
        telefone = input("Digite o novo telefone: ").strip()
        email = input("Digite o novo e-mail: ").strip()
        agenda[nome] = [telefone, email]
        print("Contato atualizado com sucesso!")
    else:
        print("Contato não encontrado!")

def remover_contato(agenda):
    nome = input("Digite o nome do contato a ser removido: ").strip()
    if nome in agenda:
        del agenda[nome]
        print("Contato removido com sucesso!")
    else:
        print("Contato não encontrado!")

def exibir_todos_contatos(agenda):
    if not agenda:
        print("Agenda vazia!")
    else:
        print("\nLista de Contatos:")
        for nome, dados in agenda.items():
            print(f"Nome: {nome} | Telefone: {dados[0]} | E-mail: {dados[1]}")

def main():
    agenda = {}
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            adicionar_contato(agenda)
        elif opcao == "2":
            buscar_contato(agenda)
        elif opcao == "3":
            editar_contato(agenda)
        elif opcao == "4":
            remover_contato(agenda)
        elif opcao == "5":
            exibir_todos_contatos(agenda)
        elif opcao == "6":
            print("Saindo da agenda. Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
