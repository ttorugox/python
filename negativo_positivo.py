#ESSA É A FORMA SIMPLIFICADA DESSE COMANDO, A FORMA ENSINADA POR ALESSANDRO È OUTRA
    #Peça um número inteiro ao usuário e verifique se é positivo, negativo ou  zero
numero = int(input("Digite um número: "))

#Verificação do número
if numero < 0:
    print(f"{numero} é um número negativo. ")
elif  numero > 0:
    print(f"{numero} é um número é positivo. ")
else:
    print("Esse número é zero ")