'''Colocar tudo em maiúsculo, minúsculo, somente primeira letra de cada palavra em maiúsculo'''

stop = False
while not stop:
    text = input("Texto: ")
    #text = "Locação de imóvel situado na Avenida São José"
    words = text.split()
    new_text = ""
    print("Para finalizar insira 0")
    try:
        option = int(input(
            "1- Colocar tudo em maiúsculo\n2- Colocar tudo em minúsculo\n3-Colocar somente a primeira letra de cada palavra em maiúsculo\n"))
        if option == 0:
            print("Finalizado pelo usuário")
            stop = True
            break
    except ValueError:
        print("Valor inválido")

    for word in words:
        if option == 1:
            new_text += " "
            for letter in word:
                if letter.isalpha():
                    new_text += letter.upper()
                    continue
                new_text += letter
        if option == 2:
            new_text += " "
            for letter in word:
                if letter.isalpha():
                    new_text += letter.lower()
                    continue
                new_text += letter
        if option == 3:
            new_text += " "
            for i in range(len(word)):
                if word[i].isalpha() and i == 0:
                    new_text += word[i].upper()
                else:
                    new_text += word[i]
    print(new_text.strip())

print("Obrigado e até a próxima!")