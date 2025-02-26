
import re 

"""
    Compactaçao de Strings

    Objetivo: Criar uma função que compacta uma string repetitiva usando um formato reduzido, semelhante a um algoritmo de Run-Length (RLE)

    O que ele deve fazer?

    - A função deve compactar sequências repetitidas de caracteres.
    - Exemplo de entrada: "aaabbcccd"
    - Exemplo de saída: "a3b2c4d1"

"""

# Função que tem objetivo de compactar palavras

def compactar():
    print("");

# Pedir ao usuário para digitar palavras e armazenar em uma lista
padrao = r"(\w)\1+";
guardar_letras_repetidas = [0]
palavras = input("Digite quantas letras ou palavras quiser:");


# Laço para iterar em cada palavra
for contador in guardar_letras_repetidas:
    # print(contador, "contador")


    # Tamanho da String digitada pelo usuário
    tamanho = len(palavras)
    print(tamanho, "tamanho da String");

    # Verificando se a String contém caracteres repetitivos

    # TODO Entender sobre Expressões Regulares para identificar palavras com padrões

    repeticoes = re.findall(padrao, palavras)

    if repeticoes :
        print(f"Possui letras repetitivas! \n Letras repetidas: {repeticoes}")
    else:
        print("Não possui letras repetitivas")
        
    # TODO Entender sobre: from collections (import Counter) e (import string)

    resultado = "";
    contador = 1;

    for i in range(len(palavras)):
        if i + 1 < len(palavras) and palavras[i] == palavras[i + 1]:
            contador += 1  # Conta repetições
        else:
            resultado += palavras[i] + str(contador) 
            contador = 1 

    print(f"Compactação: {resultado}")

# Chamada da função
compactar();

