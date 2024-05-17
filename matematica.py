    #Solicite ao usuário para digitar dois números e realize as quatro operações básicas
def main():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    #Menu de operações
    print("\nEscolha a operação desejada: ")
    print("1 - adicao")
    print("2 - subtracao")
    print("3 - multipicacao")
    print("4 - divisao")

    #Solicite a escolha da operação
    operacao = int(input("Digite sua escolha (1, 2, 3 e 4): "))

    #Realize a operação escolhida
    if operacao == 1:
        resultado = num1 + num2
        operador = "+"
    elif operacao == 2:
        resultado = num1 - num2
        operador = "-"
    elif operacao == 3:
        resultado = num1 * num2
        operador = "*"
    elif operacao == 4:
        resultado = num1 / num2
        operador = "/"
    else:
        print("Operação inválida!")
        return
    
    #Imprimi o resultador
    print(f"{num1} {operador} {num2} = {resultado:.2f}")

if __name__ == "__main__":
    main()