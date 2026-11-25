import random

def exibir(A, B, C, D, E, F, G, placar, vidas, letras_utilizadas):
    print(A)
    print(B)
    print(C)
    print(D, "    ", "  ".join(placar))
    print(E)
    print(F)
    print(G,"Vidas = ", vidas)
    print("Letras utilizadas:", " - ".join(letras_utilizadas), "\n\n")
    return None

def somente_letra(palavra_secreta, letras_utilizadas) -> str:
    while True:
        palpite = input("Dê o seu palpite: ").upper()
        if palpite.isalpha() and (len(palpite) == 1 or len(palpite) == len(palavra_secreta)):
            if len(palpite) == len(palavra_secreta):
                confirmar = input("Confirmar tentativa de adivinhar a palavra secreta? S\n").upper()
                if confirmar == "S":
                    pass
                else:
                    continue
            if palpite in letras_utilizadas:
                print("Essa letra já foi utilizada. Escolha outra.")
                continue
            return palpite        
        else:
            print("Valor inválido. Tente novamente.")


def main() -> None:
    continuar_jogo = True
    palavras = ["alameda","alambrado","alopatia","altissonante","aportuguesamento","arquitetura","artesanato","bracelete","brancura","boxeador","braquiossauro","camaradagem","carrapaticida","chocadeira","claustrofobia","classificado","coeficiente","algoritmo","condimento","correspondente","insalubridade"]
    print(''.center(47, "#"))
    print('  Jogo da Forca  '.center(47, "#"))
    print(''.center(47, "#"),"\n")    

    while continuar_jogo == True:    
        palavra_secreta = random.choice(palavras).upper()
        A = "+------+"
        B = "|         "
        C = "|         "
        D = "|         "
        E = "|         "
        F = "|         "
        G = "-\-\-\-\-\-\-\-\ "
        H = ("_" * len(palavra_secreta))
        placar = []
        for traço in H:
            placar.append(traço)
        letras_utilizadas = []    

        print("Você consegue descobrir a palavra correta em menos de 7 tentativas?")
        vidas = 7  
        while True:
            exibir(A, B, C, D, E, F, G, placar, vidas, letras_utilizadas)
            palpite = somente_letra(palavra_secreta, letras_utilizadas)
            if len(palpite) == len(palavra_secreta):
                if palpite == palavra_secreta:
                    print("Parabéns! Você venceu!")
                    print("A palavra é: ", palavra_secreta)
                    print("Ainda sobraram ", vidas, " vidas.")
                    break
                else: 
                    print("Além de não saber muito ainda é apressado... Melhore!")
                    break
            else:
                letras_utilizadas.append(palpite)
                acertos = 0
                for i in range(len(palavra_secreta)):
                    if palavra_secreta[i] == palpite:
                        acertos += 1
                        placar[i] = palpite
                if acertos == 0:
                    vidas -= 1
                    if vidas == 6:
                        B ="|    ( )    "
                    elif vidas == 5:
                        C = "|     |   "
                    elif vidas == 4:
                        C = "|    /|    "
                    elif vidas == 3:
                        C = "|    /|\  "
                    elif vidas == 2:
                        D = "|    /    "
                    elif vidas == 1:
                        D = "|    / \  "
                if placar == list(palavra_secreta):
                    print("Parabéns, você venceu!")
                    print("A palavra é: ", palavra_secreta)
                    print("Ainda sobraram ", vidas, " vidas.")
                    break
                if vidas == 0:
                    print("Vidas = ", vidas)
                    print("Você é uma decepção!")
                    print("A palavra era ", palavra_secreta)
                    break
           
        if input("Continuar? [S/n]    ").upper() != "S":
            continuar_jogo = False
        print("\n")
    print("Fim de jogo.\nAté a próxima!")

main()

