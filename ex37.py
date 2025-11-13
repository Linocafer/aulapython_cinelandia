# Defina um número secreto (por exemplo, 42). Crie um programa que peça ao usuário para adivinhar esse número. 
#Use um loop while para repetir a pergunta até que o palpite esteja correto. 
# Use instruções if, elif e else para dar dicas ao usuário: "Muito alto", "Muito baixo" ou "Parabéns!".

numero_secreto = 42
palpite = 0

print("Tente adivinhar o número secreto entre 1 a 1000")

while palpite != numero_secreto:
    try:
        entrada = input("Seu palpite: ")
        palpite = int(entrada)

        if palpite < numero_secreto: 
            print("Muito baixo. Tente um número maior")
        elif palpite > numero_secreto:
            print("Muito alto. Tente um número menor")
        else:
            print(f"Parabéns! Você acertou o número secreto: {numero_secreto}!")
    except ValueError:
        print("Por favor, digite apenas números inteiros.")
        
