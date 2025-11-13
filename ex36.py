# Crie um programa que peça ao usuário para digitar números repetidamente. O programa deve parar de pedir números quando o usuário digitar 0. A cada número digitado, 
# use um if para verificar se ele é positivo. O programa deve somar apenas os números positivos e, no final, exibir o resultado da soma.

soma_positivos = 0
numero = -1  # valor inicial diferente de 0 para entrar no loop

while numero != 0:
    entrada = input("Digite um número (0 para parar): ")

    try:
        numero = int(entrada)
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
        continue  # volta para o início do loop

    if numero > 0:
        soma_positivos += numero

print(f"A soma dos números positivos é: {soma_positivos}")

