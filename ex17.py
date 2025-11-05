# Uma loja de produtos tecnologicos te contratou para desenvilver um código da seguinte forma:
# Leia um Produto e de acordo com o produto verique o preço. (Vide a tabela abaixo)
# Mouse:  10 // Teclado: 20 // memoria: 100
# Leia ainda a quantiade de produtos comprados:
# Calcule: total = preço * quantidade
# Imposto = se a quantidade for maior que 10 cacule um imposto de 5% sobre o total senão calcule 10%
# Valor final = total+ imposto

# Leitura do nome do produto
produto = input("\nDigite o nome do produto (Mouse, Teclado ou Memoria): ").upper()

# Define o preço conforme a tabela
if (produto == "MOUSE"):
    preco = 10
elif (produto == "TECLADO"):
    preco = 20
elif (produto == "MEMORIA"):
    preco = 100
else:
    preco = 0
    print ("Produto inválido")
    exit()

# Lê a quantidade comprada
quantidade = int(input("\nQuantidade que deseja levar: ")) 

# Calcula o total
total = preco * quantidade

# Calcula o imposto
if (quantidade > 10):
    imposto = total * 0.05  # 5%
else:
    imposto = total * 0.10  # 10%
    
# Calcula o valor final
Valor_Final = total + imposto

#Exibir resultado final
print("\n----- Nota fiscal ------")
print(f"Produto: {produto}")
print(f"Preço Unitário: R$ {preco: .2f}")
print(f"Quantidade: {quantidade}")
print(f"Valor: R$ {total: .2f} ")
print(f"Imposto cobrado: R$ {imposto: .2f}")
print(f"Valor c/ Imposto: R$ {Valor_Final: .2f}")





                      

