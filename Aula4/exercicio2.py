def exibir_menu():
    print("\nMENU - SISTEMA DE NOTAS")
    print("1. Cadastrar Aluno e Nota")
    print("2. Exibir Média da Turma")
    print("3. Exibir Alunos Acima da Média")
    print("4. Exibir Maior e Menor Nota")
    print("5. Sair")

def cadastrar_aluno(alunos):
    nome = input("Digite o nome do aluno: ").strip()
    if nome in alunos:
        print("Aluno já cadastrado!")
        return
    try:
        nota = float(input("Digite a nota do aluno: "))
        alunos[nome] = nota
        print("Aluno cadastrado com sucesso!")
    except ValueError:
        print("Nota inválida! Digite um número válido.")

def calcular_media(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado!")
        return None
    return sum(alunos.values()) / len(alunos)

def exibir_media_turma(alunos):
    media = calcular_media(alunos)
    if media is not None:
        print(f"Média da turma: {media:.2f}")

def exibir_acima_da_media(alunos):
    media = calcular_media(alunos)
    if media is not None:
        acima_da_media = {nome: nota for nome, nota in alunos.items() if nota > media}
        if acima_da_media:
            print("Alunos acima da média:")
            for nome, nota in acima_da_media.items():
                print(f"{nome}: {nota:.2f}")
        else:
            print("Nenhum aluno acima da média.")

def exibir_maior_menor_nota(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado!")
        return
    maior_aluno = max(alunos, key=alunos.get)
    menor_aluno = min(alunos, key=alunos.get)
    print(f"Maior nota: {maior_aluno} - {alunos[maior_aluno]:.2f}")
    print(f"Menor nota: {menor_aluno} - {alunos[menor_aluno]:.2f}")

def main():
    alunos = {}
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            cadastrar_aluno(alunos)
        elif opcao == "2":
            exibir_media_turma(alunos)
        elif opcao == "3":
            exibir_acima_da_media(alunos)
        elif opcao == "4":
            exibir_maior_menor_nota(alunos)
        elif opcao == "5":
            print("Saindo do sistema de notas. Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
