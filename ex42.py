def ehpar(n):
    return n % 2 == 0  # Retorna True se n for par, False se for ímpar

num = int(input("Digite um número inteiro: "))
resultado = ehpar(num)  # Chama a função e guarda o resultado

if resultado:  # Se resultado for True (n é par)
    print(f"O número {num} é par")
else:  # Se resultado for False (n é ímpar)
    print(f"O número {num} é impar")


