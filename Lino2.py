#escreva um programa que um numero inteiro. Se o numero for par (ou seja, o resto da divisão por 2 é 0) imprima o numero par
# Lê um número inteiro do usuário
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é par
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é impar.")