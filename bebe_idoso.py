    #Solicite a idade do usuário
def main():
    idade = int(input("Digite sua idade: "))

    #Verefique se a pessoa é bebê, criança, adolescente, adulto ou idoso
    if idade < 0:
        print("Idade inválida!")
    elif idade <= 2:
        print("Bebê")
    elif idade <= 12:
        print("Criança")
    elif idade <= 17:
        print("Adolescente")
    elif idade <= 64:
        print("Adulto")
    else:
        print("Idoso")
if __name__ == "__main__":
    main()