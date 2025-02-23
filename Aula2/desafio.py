""" 

Criar um Sistema de cadastro e Análise de Idades.

O programa deve permitir que usuários múltiplas pessoas, armazenem nome e idade. Em seguida, o sistema deve calcular estatísticas sobre os dados inseridos.

================================================================

"""

# O usuário deve cadastrar quantas pessoas quiser
cadastros = []
distincaoIdade = []

while True:
    print("Deseja cadastrar mais uma pessoa? (s/n)");
    resposta = str(input());

    transformaResposta = resposta.lower()

    # Só conferindo se estava transformando tudo o que o usuário estava digitando
    # print(transformaResposta, "transformaResposta")


    if resposta =="n" or resposta == "sair":
        break;

    elif resposta == "s":


        #Solicitar nome e idade de cada pessoa

        print("Digite seu nome:");
        nome = str(input());

        print("Digite sua idade:");
        idade = int(input());


        # Guardar os dados em uma lista de dicionários
        cadastros.append({"nome": nome,"idade": idade})
        print(f"Pessoa cadastrada: {nome} idade do individuo cadastrado: {idade}");
        
        # Pessoa mais velha e mais nova
        
        if idade >=18 :
            print("Maior de idade")

        else :
            print("Menor de idade")
    
    else:
        print("Resposta inválida. Por favor, responda com 's' para sim ou 'n' para não.");
#Fim de cadastro de pessoas


# Após o cadastro, exiba as seguintes estatísticas


#Pessoa mais velha e mais nova

pessoa_mais_velha = cadastros[0];
pessoa_mais_nova = cadastros[0];

for pessoa in cadastros :
    if pessoa["idade"] > pessoa_mais_velha["idade"] :
        pessoa_mais_velha = pessoa;

    if pessoa["idade"] < pessoa_mais_nova["idade"]:
        pessoa_mais_nova = pessoa;


# Média de idade do grupo
soma_idades = 0
for pessoa in cadastros :
    soma_idades += pessoa["idade"]

media_idades = soma_idades / len(cadastros)



# Número de menores de idade (< 18 anos)
menores_idade = 0
for pessoa in cadastros :
    if pessoa["idade"] < 18 :
        menores_idade += 1

# Número de idosos (>= 60 anos)
numero_idosos = 0

for pessoa in cadastros :
    if(pessoa["idade"] >= 60) :
        numero_idosos += 1


# Total de pessoas cadastradas
print(f"Total de pessoas cadastradas: {len(cadastros)}")
print(f"A pessoa cadastrada: {pessoa_mais_nova["nome"]} é a mais nova")
print(f"A pessoa cadastrada: {pessoa_mais_velha["nome"]} é a mais velha")
print(f"Média de idade do grupo: {media_idades} anos")
print(f"Número de menores de idade: {menores_idade}")
print(f"Número de idosos: {numero_idosos}")