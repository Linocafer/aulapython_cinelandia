# Crie uma função que receba dois numeros e retorne o maior deles.
def maior(a,b):
    if a > b:
        return a
    else:
        return b
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print(f"O maior número é {maior(num1, num2)}")

