

"""
    Analisador de Texto 

    Objetivo: Criar uma função que analisa um texto longo e retorna as cinco palavras mais frequentes, ignorando palavras comuns (stopwords)

    O que ele deve fazer?

    - O programa deve processar um texto digitado pelo usuário.

    - Deve remover pontuações e converter texto para minúsculas.

    - Deve ignorar palavras muito comuns, como "de","o","a","e","que","com" etc

    - Deve conter as cinco palavras mais frequentes no texto.


"""
import re
from collections import Counter

def analisar_texto(texto):
    stopwords = {"de", "o", "a", "e", "que", "com", "do", "da", "em", "um", "para", "se", "na", "no"}
    
    texto_limpo = re.sub(r'[^\w\s]', '', texto.lower()) 
    palavras = texto_limpo.split() 
    palavras_filtradas = [palavra for palavra in palavras if palavra not in stopwords] 
    
    contagem = Counter(palavras_filtradas)  
    mais_comuns = contagem.most_common(5) 
    
    return mais_comuns

# Exemplo de uso:
texto = "Só sei que nada sei e o que não sei aprenderei! E dito o que aprenderei aperfeiçoarei!"
print(analisar_texto(texto))