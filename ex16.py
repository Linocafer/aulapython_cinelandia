#Desenvolva um código python que liea um cargo de funcionario, de acordo com o cargo mostre o salario vide a tabela abaixo:
    #caixa = 1500
    #Vendedor = 2400
    #Gerente = 4000
    # De acordo com salarios acima , calcule o INSS = 12% sobre o salario // IRRF se o salario for maior de 2000 o irrf de 14% sobre o salario, senão será 8% 
    #salario final = salario - irrf - inss

# Leitura do cargo do funcionário
cargo = input(f"\nDigite o cargo do funcionário (Caixa, Vendedor ou Gerente): ").upper()

# Definindo os salários conforme o cargo
if (cargo == "CAIXA"):
    salario = 1500
elif (cargo == "VENDEDOR"):
    salario = 2400
elif (cargo == "GERENTE"):
    salario = 4000
else: 
    salario=0
    print("Cargo não existe")
    exit()

#Cálculo do INSS (12%)
inss = salario * 0.12    

# Cálculo do IRRF
if (salario > 2000):
    irrf = salario * 0.14
else:
    irrf = salario * 0.08

# Salário final
salario_final = salario - inss - irrf

# Exibição dos resultados
print(f"\n--- Demonstrativo de Pagamento ---")
print(f"Cargo: {cargo}")
print(f"Salário bruto: R${salario: .2f}")
print(f"INSS (12%): R${inss: .2f}")
print(f"IRRF ({'14%' if salario > 2000 else '8%'}): R${irrf: .2f}")
print(f"Salário líquido: R${salario_final: .2f}")
