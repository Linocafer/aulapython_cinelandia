soma = 0
contador = 0
nota = float(input("Digite uma nota (-1 para sair): "))

while nota != -1:
    soma += nota
    contador += 1
    nota = float(input("Digite outra nota (-1 para sair): "))

if contador > 0:
    print("Média =", soma / contador)
else:
    print("Nenhuma nota digitada.")
