# Vai printar todas os itens da lista

frutas = ["banana", "maçã", "pera"]

for fruta in frutas:
    print(fruta)



# Vai printar do número 0 ao 4
for i in range(5):
    print(i)



# Vai printar a primeira letra dessa minha string
palavra = "melancia"

letarTeste = palavra[0]
print(letarTeste)


# Aqui vai printar quando o loop for na 7ª letra da palavra "melancia"
for letra in palavra[6]:
    print(letra)


# Sintaxe padrão do loop while
i = 1
while i < 6 :
    print(i, "teste de loop while")
    i+=1;

# Nesse caso eu estou fazendo uma verificaçaõ quando o loop chega em 3 e quando é igual a esse valor ele para e print "Loop interrompido"
i2 = 0
while i2 < 6:
    print(i2, "teste de loop while2")
    if i2 == 3:
        print("Loop interrompido")
        break
    i2 += 1

    # TODO Só fico meio confusa em relação onde colocar esse incremento dentro desses loops