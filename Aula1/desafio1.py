# Crie um programa que permita ao usuário escolher entre as seguintes conversões:

# - Celsius para Farenheit
# - Quilômetros para Milhas
# - Gramas para quilogramas

# * Solicite o valor a ser convertido e exiba o resultado formatado.

print("Escolha o que deseja calcular primeiro: \n", "1.Celcius para Farenheit \n","2.Quilômetros para Milhas \n", "3.Gramas para Quilogramas \n", "Digite 1, 2 e 3 para fazer a sua escolha")
selecionarAcao = int(input());

if(selecionarAcao == 1):
    print("Você escolheu Celsius para Farenheit");

    #Fórmula : F = C x 1,8 + 32
    valorCelcius = float(input("Digite o valor a ser convertido para Farenheit:"));

    valorFinal = valorCelcius * 1.8 + 32;

    print("Valor final:", f"{valorFinal:.1f}F");


elif(selecionarAcao == 2):
    print("Você escolheu Quilômetros para Milhas");

    milhas = float(input("Digite o valor a ser convertido:"));
    NUMEROMILHAS = 0.621371;
    valorFinal = milhas * NUMEROMILHAS;
    print("Valor convertido:", f"{valorFinal:.2f} milhas")

elif(selecionarAcao == 3):
    print("Você escolheu Gramas para Quilogramas");

    gramas = float(input("Digite o valor a ser convertido:"));

    kilogramas = gramas / 1000;

    print("Valor convertido:", f"{kilogramas:.2f}Kg")


#TODO Esta bem desorganizado no terminal os prints, mas funcional, pode ser uma melhoria para mais tarde