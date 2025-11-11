# Desenvolva um código python usando while que digite um nome e imprima, só para programa a dgitar sar em maiscula
nome = ""
while nome != "SAIR":
    nome = input("Digite um nome (ou 'sair' para encerrar): ").upper()  
    if nome == "SAIR":
        break #sair do laço while
    print(f"Olá, {nome}")


 


 
