# Solicita dois valores do usuário
v1 = int(input("Digite um valor: "))
v2 = int(input("Digite outro valor: "))

# Verifica qual é o maior
if v1 > v2:
    print(f"{v1} é maior que {v2}.")
elif v2 > v1:
    print(f"{v2} é maior que {v1}.")
else:
    print("São iguais")
