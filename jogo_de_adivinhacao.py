import random

print("---------------------------------")
print("Bem-vindo ao jogo de adivinhação!")
print("---------------------------------")

#váriaveis
numero_secreto = random.randrange(1,101)
total_de_tentativas = 0
pontos = 1000

print("Qual nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difício")

nivel = int(input("Define o nível: "))


if (nivel == 1):
    total_de_tentativas = 20

elif (nivel == 2):
     total_de_tentativas = 10
     
else:
    (nivel == 3)
    total_de_tentativas = 3

#lógica
#while(enquanto) é uma das estruturas de repetição no python. Com ela, você consegue executar um bloco de códigos enquanto determina uma condição verdadeira para ele.
for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou " , chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

#condições
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

#resultado
    if(acertou):
        print("**** Você acertou e fez {} pontos! ****".format(pontos))
        break
    else:
        if(maior):
            print("**** Você errou! Dica: O seu chute foi maior do que o número secreto ****")
        elif(menor): 
            print("**** Você errou! Dica: O seu chute foi menor do que o número secreto ****")
        pontos_perdidos = abs(numero_secreto - chute)  #40-20 = 20
        pontos = pontos - pontos_perdidos

print("Fim do jogo.")



