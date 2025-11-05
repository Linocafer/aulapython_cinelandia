#Desenvolva o codigo python se a temperatura está frio, agradavel ou calor. Siga a tabela abaixo?
# Menor que 18 - frio /// Entre 18 a 30 - agradavel /// maior que 30 - calor
# Lê a temperatura digitada pelo usuário
temperatura = float(input("Digite a temperatura: "))
# Verifica a faixa de temperatura
if (temperatura >=10 and temperatura < 18):
    print("Frio")
elif (temperatura >=18 and temperatura <30):
    print("Agradável")
elif (temperatura > 30):
    print("Calor")
elif (temperatura > 0 and temperatura < 10):
    print("Muito frio")   
elif (temperatura <= 0): 
    print("Congelante") 


        



