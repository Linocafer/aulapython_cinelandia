# Formulário de Dados Cadastrais - Terminal

print("=== Formulário de Cadastro ===")

time = input ("Para qual time você torce? ")
nome = input("Nome completo: ")
idade = input("Idade: ")
email = input("E-mail: ")
telefone = input("Telefone: ")
endereco = input("Endereço: ")

print("\n=== Dados Cadastrados ===")
print(f"Time: {time}")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"E-mail: {email}")
print(f"Telefone: {telefone}")
print(f"Endereço: {endereco}")

# Opcional: salvar os dados em um arquivo
with open("cadastro.txt", "a", encoding="utf-8") as f:
    f.write(f"{nome};{idade};{email};{telefone};{endereco}\n")

print("\nDados salvos em 'cadastro.txt'")
