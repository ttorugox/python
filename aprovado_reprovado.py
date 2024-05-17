#ESSA É A FORMA SIMPLIFICADA DESSE COMANDO, A FORMA ENSINADA POR ALESSANDRO È OUTRA
    #Calcula a média e verifica a situação
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1 + n2 + n3) / 3

situacao = "Aprovado" if media >= 7 else "Reprovado"
print(f"Sua média final é {media:.2f} e você está {situacao}.")
