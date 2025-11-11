#Desenvolva um código python que leia 5 numeros e diga se cada numero ao momento que for lido se é par ou impar
for i in range(1,6):
    n = int(input(f"Digite o {i}º número: "))
    if n % 2 == 0:
        print(f"O número {n} é PAR.\n")
    else:
        print(f"O número {n} é ÍMPAR.\n")
