#desenvolver um código python que leia dois nomes
#nomes se o primeiro nome for senac ou
#segundo nome for cinelandia imprimir SENAC
#senão imprimir não é senac
nome1=input("digite o primeiro nome")
nome2=input("digite o segundo nome")
if (nome1 == "senac" or nome2 == "cinelandia"):
    print(f"Bem Vindo {nome1} {nome2}")
else: 
    print(f"você não é senac") 
       