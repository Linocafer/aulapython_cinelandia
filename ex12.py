#Desenvolva um código python que verifique se digitou m ou f, masculino para m e feminino para f, caso seja diferente de um dos dois dia indefinido
# Lê uma letra do usuário
genero = input("Digite seu genero (M ou F) ").upper()
# Verifica o valor digitado
if (genero == "M" or genero == "MASCULINO"):
    print("Masculino")
elif (genero == "F" or genero == "FEMININO"):
    print("Feminino")
else:
    print("Genero Não localizado")            