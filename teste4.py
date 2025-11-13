# Definição da função
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Programa principal
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = calcular_imc(peso, altura)
print(f"Seu IMC é: {imc:.2f}")

# Classificação do IMC
if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 25:
    print("Seu peso está normal.")
elif imc < 30:
    print("Você está com sobrepeso.")
else:
    print("Você está com obesidade.")


