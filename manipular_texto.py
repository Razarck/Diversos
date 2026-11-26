# O código tem como objetivo receber como inputs texto e exibi-lo nas seguintes opções:
# Todo maiúsculo
# Todo minúsculo
# Somente a primeira letra de cada palavra em maiúsculo e as restantes em minúsculo

def check_input() -> int | bool:
    message = "Para finalizar insira 0\n1- Colocar tudo em maiúsculo\n2- Colocar tudo em minúsculo\n3- Colocar somente a primeira letra de cada palavra em maiúsculo\n"
    valid_options = [0,1,2,3]
    while True:
        try:
            option = int(input(message))
            if option not in valid_options:
                raise ValueError
            if option == 0:
                return False
            return option
        except  ValueError:
            print("Valor inválido!\nTente novamente")

def check_text() -> str:
    message = "Insira o texto.\n"
    while True:
        try:
            text = input(message)
            if len(text) < 2:
                raise ValueError
            return text
        except  ValueError:
            print("Texto inválido!.\nTente novamente")
    
def run_words(option: int, text: str) -> None:
    words = text.split()
    new_text = ""
    for word in words:
        new_text += " "
        for i in range(len(word)):
            #print(word[i], i)
            if option == 1:
                new_text += case_upper(word[i])
            if option == 2:
                new_text += case_lower(word[i])
            if option == 3:
                new_text += case_other(word[i], i)        
    print(new_text.strip())
    return None

def case_upper(letter: str) -> str:
    if letter.isalpha():
        return letter.upper()
    return letter

def case_lower(letter: str) -> str:
    if letter.isalpha():
        return letter.lower()
    return letter

def case_other(letter: str, i: int) -> str:
    if letter.isalpha():
        if i == 0: return letter.upper()
        return letter.lower()
    return letter

def main() -> None:
    while True: 
        option = check_input()
        if option == 0:    break
        text = check_text()
        run_words(option, text)
    print("Obrigado e até a próxima!")

main()




