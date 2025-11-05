# Desenvolva um codigo python que leia 3 valores e mostre qual o maior
# Lê três valores do usuário
v1 = float(input("Digite um valor: "))
v2 = float(input("Digite outro valor: "))
v3 = float(input("Digite um novo valor: "))
# Verifica qual é o maior
if (v1 > v2 and v1 > v3):
    print(f"{v1} é maior")
elif (v2 > v1 and v2 > v3):
    print(f"{v2} é maior")
else:
    print(f"{v3} é maior")


