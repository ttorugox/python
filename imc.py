def calcular_imc(peso, altura):
    if altura <= 0:
        raise ValueError("Altura deve ser maior que zero")
    return peso / (altura ** 2)

def interpretar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidade grau I"
    elif imc < 40:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"
    
def main():
    try:
        peso = float(input("Informe o peso em kg: "))
        altura = float(input("Informe sua altura em metros: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite números válidos para peso e altura.")
        return
    
    imc = calcular_imc(peso, altura)
    estado_nutricional = interpretar_imc(imc)

    print(f"Seu IMC é {imc:.2f} e você com {estado_nutricional}. ")

if __name__ == "__main__":
    main()