def somar(a,b):
    return a+b

def subtrair(a,b):
    return a - b

def mult(a,b):
    return a * b

def div(a,b):
    if b != 0:
        return a / b
    else:
        print("Valor Inválido")
escolha = ""
while escolha != "0":
    escolha = input("Digite uma opção 0- parar; 1- Somar; 2- Subtrair; 3- Multiplicar, 4- Dividir: ")
    num1 = int(input("Digite o primerio número "))
    num2 = int(input("Digite outro número "))
   
    if escolha == "1":
        x=somar(num1, num2)
    elif escolha == "2":
        x= subtrair(num1, num2)
    elif escolha == "3":
        x= mult(num1, num2)
    elif escolha == "4":
        x=div(num1, num2)
    else:
        break    
 
    print(f"Resultado da operação: {x}")