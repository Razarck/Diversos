import random

def conferir_chute() -> int:
    while True:
        try:
            user_input = int(input("Digite um número entre 1 e 100: "))
            if user_input <= 0 or user_input > 100:
                raise ValueError
            return user_input
        except ValueError:
            print("valor inválido. Tente novamente")

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

jogar_novamente = True
while jogar_novamente:
    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 100

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = 0
    while nivel not in {1, 2, 3}:
        try:
            nivel = int(input("Defina o nível: "))
            if nivel not in {1, 2, 3}:
                raise ValueError
        except ValueError:
            print("Valor inválido. Por favor escolha entre as opções 1, 2 ou 3.")

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    tentativa = 1
    while tentativa <= total_de_tentativas:
        print("Tentativa {} de {}".format(tentativa, total_de_tentativas))
        chute = conferir_chute()
        print("Você digitou " , chute)
        tentativa += 1
        if chute == numero_secreto:
            print("Parabéns, você acertou!")
            break
        else:
            pontos -= 100/total_de_tentativas
            if chute > numero_secreto:
                print("O seu chute foi maior do que o número secreto.")
            else:
                print("Você errou! O seu chute foi menor do que o número secreto.")


    if pontos == 100:
        print("Pontuação máxima! Você é sinistro!")
    elif pontos == 0:
        print("Você perdeu!\nMelhore!")
    else:
        print("Pontuação: ", pontos)
    continuar = input("Jogar novamente S/n?\n")
    if continuar.upper() != "S":
        print("Até a próxima ;)")
        jogar_novamente = False
