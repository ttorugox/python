#ESSA É A FORMA SIMPLIFICADA DESSE COMANDO, A FORMA ENSINADA POR ALESSANDRO È OUTRA
    #Função celsius_para_fahrenheit: Essa função recebe um valor em Celsius como argumento.
    #A fórmula para converter Celsius para Fahrenheit é utilizada: fahrenheit = (celsius * 9/5) + 32.
    #O resultado da conversão (em Fahrenheit) é retornado pela função.

#Ela tenta converter a temperatura digitada pelo usuário para Fahrenheit:
    #Solicita a temperatura em Celsius ao usuário usando input().
    #Converte a temperatura usando a função celsius_para_fahrenheit.
    #Imprime o resultado usando formatação de string (f-string) para exibir os valores com uma casa decimal.

#Se o usuário digitar um valor inválido (não um número decimal)
    #Uma mensagem de erro é exibida usando except ValueError.

    #Converte a temperatura em Celsius para Fahrenheit.
def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

try:
    # Solicita a temperatura em Celsius ao usuário e converte para float
  celsius = float(input("Digite a temperatura em Celsius: "))

  # Converte a temperatura para Fahrenheit
  fahrenheit = celsius_para_fahrenheit(celsius)

  # Imprime o resultado
  print(f"{celsius:.1f}°C equivale a {fahrenheit:.1f}°F")
except ValueError:
  print("Valor inválido. Digite um número decimal.")