# Análise de dados com números digitados pelo usuário

numeros = []
num = float(input("Digite um número (0 para sair): "))

while num != 0:
    numeros.append(num)
    num = float(input("Digite outro número (0 para sair): "))

if len(numeros) > 0:
    media = sum(numeros) / len(numeros)
    print("\n--- Resultados ---")
    print("Quantidade de números:", len(numeros))
    print("Média:", media)
    print("Maior número:", max(numeros))
    print("Menor número:", min(numeros))
else:
    print("Nenhum número foi digitado.")
