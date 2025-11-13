#crie uma função que receba o lado de um quadrado e retorne o valor da sua área ($A - lado^2$)
def quadrado(lado):
    return lado ** 2  # Calcula o quadrado do lado

#Interação do usuário
medida_lado = float(input("Digite a medida do lado do quadrado: "))

# chamada da função exibição do resultado
area = quadrado(medida_lado)  
print(f"A área do quadrado é: {area}")

