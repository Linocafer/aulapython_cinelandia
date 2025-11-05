# Lê um valor digitado pelo usuário
v = float(input("Digite um valor: "))

# Verifica se o número é positivo, negativo ou zero
if v > 0:
    print(f"{v} é um valor positivo.")
elif v < 0:
    print(f"{v} é um valor negativo.")
else:
    print("O número é zero.") 