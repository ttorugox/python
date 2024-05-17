#ESSA É A FORMA SIMPLIFICADA DESSE COMANDO, A FORMA ENSINADA POR ALESSANDRO È OUTRA
    #Solicite o salário de um funcionário
    #Solicite o valor de aumento do salário
    #Calcule o novo salário com base no aumento
def calcular_aumento_salarial(salario, aumento_absoluto):
    novo_salario = salario + aumento_absoluto
    porcentagem_aumento = (aumento_absoluto / salario) * 100
    return novo_salario, porcentagem_aumento

def main():
    salario = float(input("Informe o seu salário atual: "))
    aumento_absoluto = float(input("Informe o valor do seu aumento salarial: "))

    novo_salario, porcentagem_aumento = calcular_aumento_salarial(salario, aumento_absoluto)

    print(f"O novo salário do funcionário é de R${novo_salario:.2f}.")
    print(f"O aumento salarial foi de {porcentagem_aumento:.2f}%.")

if __name__ == "__main__":
    main()