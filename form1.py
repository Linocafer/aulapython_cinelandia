import tkinter as tk
from tkinter import messagebox

def salvar_dados():
    time = entrada_time.get()
    nome = entrada_nome.get()
    idade = entrada_idade.get()
    email = entrada_email.get()
    telefone = entrada_telefone.get()
    endereco = entrada_endereco.get()

    if not nome or not email:
        messagebox.showwarning("Aviso", "Preencha pelo menos o nome e o e-mail!")
        return

    with open("cadastros.csv", "a", encoding="utf-8") as f:
        f.write(f"{time};{nome};{idade};{email};{telefone};{endereco}\n")

    messagebox.showinfo("Sucesso", "Cadastro salvo com sucesso!")
    entrada_time.delete(0,tk.END)
    entrada_nome.delete(0, tk.END)
    entrada_idade.delete(0, tk.END)
    entrada_email.delete(0, tk.END)
    entrada_telefone.delete(0, tk.END)
    entrada_endereco.delete(0, tk.END)

# Criação da janela
janela = tk.Tk()
janela.title("Formulário de Cadastro")
janela.geometry("400x350")

# Campos
tk.Label(janela, text="Nome completo:").pack()
entrada_nome = tk.Entry(janela, width=40)
entrada_nome.pack()

tk.Label(janela, text="Idade:").pack()
entrada_idade = tk.Entry(janela, width=40)
entrada_idade.pack()

tk.Label(janela, text="E-mail:").pack()
entrada_email = tk.Entry(janela, width=40)
entrada_email.pack()

tk.Label(janela, text="Telefone:").pack()
entrada_telefone = tk.Entry(janela, width=40)
entrada_telefone.pack()

tk.Label(janela, text="Endereço:").pack()
entrada_endereco = tk.Entry(janela, width=40)
entrada_endereco.pack()

# Botão
tk.Button(janela, text="Salvar Cadastro", command=salvar_dados).pack(pady=10)

# Executa
janela.mainloop()

