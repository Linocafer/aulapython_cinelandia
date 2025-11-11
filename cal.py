def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

def calculadora():
    print("=== Calculadora Python ===")
    print("Operações disponíveis: +, -, *, /")
    
    while True:
        num1 = float(input("Digite o primeiro número: "))
        operador = input("Digite o operador (+, -, *, /) ou 'sair' para encerrar: ")
        if operador.lower() == 'sair':
            print("Encerrando calculadora...")
            break
        num2 = float(input("Digite o segundo número: "))

        if operador == '+':
            resultado = soma(num1, num2)
        elif operador == '-':
            resultado = subtracao(num1, num2)
        elif operador == '*':
            resultado = multiplicacao(num1, num2)
        elif operador == '/':
            resultado = divisao(num1, num2)
        else:
            print("Operador inválido!")
            continue
        
        print(f"Resultado: {resultado}\n")

calculadora()
import tkinter as tk

def adicionar_numero(numero):
    display_var.set(display_var.get() + str(numero))

def calcular():
    try:
        resultado = eval(display_var.get())
        display_var.set(resultado)
    except:
        display_var.set("Erro")

def limpar():
    display_var.set("")

# Cria janela
janela = tk.Tk()
janela.title("Calculadora Python")

display_var = tk.StringVar()

# Display
display = tk.Entry(janela, textvariable=display_var, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4)
display.grid(row=0, column=0, columnspan=4)

# Botões
botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

for (text, row, col) in botoes:
    if text == '=':
        tk.Button(janela, text=text, padx=20, pady=20, command=calcular).grid(row=row, column=col)
    elif text == 'C':
        tk.Button(janela, text=text, padx=20, pady=20, command=limpar).grid(row=row, column=col)
    else:
        tk.Button(janela, text=text, padx=20, pady=20, command=lambda t=text: adicionar_numero(t)).grid(row=row, column=col)

janela.mainloop()

