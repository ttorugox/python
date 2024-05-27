#Questão 1
while True:
    qtd_numeros = int(input("Digite a quantidade de números que você deseja verificar (digite 'x' para encerrar): "))
    
    if qtd_numeros == 'x':
        print("Programa encerrado.")
        break
    
    for i in range(qtd_numeros):
        numero = float(input("Digite o número: "))
        
        if numero > 0:
            print("O número", numero, "é positivo.")
        elif numero < 0:
            print("O número", numero, "é negativo.")
        else:
            print("O número", numero, "é zero.")


#Questão 2
while True:
    qtd_numeros = input("Digite a quantidade de números que você deseja verificar (digite 'x' para encerrar): ")

    if qtd_numeros == 'x':
        print("Programa encerrado.")
        break

    qtd_numeros = int(qtd_numeros)

    for _ in range(qtd_numeros):
        numero = int(input("Digite o número: "))

        if numero % 2 == 0:
            print("O número", numero, "é par.")
        else:
            print("O número", numero, "é ímpar.")

#Questão 3
soma = 0
for numero in range(1, 101):
    soma += numero

print("A soma de todos os números de 1 a 100 é:", soma)


#Questão 4
contador_impares = 0
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("O número", numero, "é par.")
else:
    print("O número", numero, "é ímpar.")
    contador_impares += 1

    for numero_impar in range(numero + 2, numero + 12, 2):
        print("Próximo número ímpar:", numero_impar)
        contador_impares += 1
        
        if contador_impares == 5:
            break


#Questão 5
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

menor_numero = numero1

if numero2 < menor_numero:
    menor_numero = numero2
if numero3 < menor_numero:
    menor_numero = numero3

print("O menor número digitado é:", menor_numero)

for i in range(1, menor_numero + 1):
    print("Número:", i, "- Par" if i % 2 == 0 else "- Ímpar")


#Questão 6
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

soma_pares = 0

if numero1 < numero2:
    inicio = numero1
    fim = numero2
else:
    inicio = numero2
    fim = numero1

print("Números pares entre", inicio, "e", fim, ":")

for numero in range(inicio, fim + 1):
    if numero % 2 == 0:
        print(numero)
        soma_pares += numero

print("A soma dos números pares é:", soma_pares)

