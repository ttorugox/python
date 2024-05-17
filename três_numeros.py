#ESSA É A FORMA COMPLEXA DESSE COMANDO, A FORMA ENSINADA POR ALESSANDRO È OUTRA
def main():
    # Solicita os números do usuário
    # Lista para armazenar os números
  numeros = []
  for i in range(5):
    numero = float(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

  # Determina o maior número
  menor = min(numeros)

  # Imprime o maior número
  print(f"O menor número é {menor}")

if __name__ == "__main__":
  main()

#Uso de lista para armazenar os números: Em vez de usar variáveis ​​separadas (num1, num2 e num3),
#o programa agora usa uma lista chamada numeros para armazenar os três números digitados pelo usuário.
#Isso torna o código mais conciso e facilita a iteração pelos números.

#Função max(): A função max() da biblioteca padrão do Python é usada para encontrar o maior número na lista numeros.
#Isso elimina a necessidade das instruções if aninhadas do código anterior.

#Loop for: Um loop for é usado para solicitar os três números do usuário e armazená-los na lista numeros.
#Isso torna o código mais legível e evita a repetição de código.

#Observações: Este programa ainda assume que o usuário digitará números válidos.
#O programa pode ser aprimorado para lidar com erros de entrada do usuário,
#como a digitação de letras ou valores não numéricos.
#Você pode modificar o programa para encontrar o menor número entre os três digitados,
#usando a função min() em vez de max().