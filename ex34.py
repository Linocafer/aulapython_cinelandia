senha = "python123"
tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    tentativa = input(f"Digite a senha (Tentativa {tentativas + 1}/{max_tentativas}): ")
    if tentativa == senha:
        print("Acesso permitido")
        break
    else: 
        print("Senha Incorreta") 
        tentativas += 1   

else: 
    print("Você excedeu o número máximo de tentativas. Acesso Bloqueado")
