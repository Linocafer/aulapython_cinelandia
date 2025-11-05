# Você foi contratado pelo exercíto para desenvolver um sistema de alistamento militar, onde se le o ano de nascimento do candidato e o genero, o sistema irá calcular a idade.
# Se a idade for maior igual a 18 e o sexo masculino ele estará apto a se alistar, senão não apto

# Lê o ano de nascimento e o gênero do candidato
ano_nasc_cand = int(input("Digite o ano de nascimento: "))
Genero = input("Digite seu genero (M ou F) ").upper()

#Calcular a idade
idade = 2025 - ano_nasc_cand
print(f"Idade: {idade} anos")

# Verifica se esta apto para alistamento
if (Genero == "M" and idade >=18):
    print("Está apto a se alistar")
else:
    print("Não apto")
