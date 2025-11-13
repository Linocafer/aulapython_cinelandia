import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from telegram import Bot
import os

# --- Configurações ---
ARQUIVO_EXCEL = "gastos_gui.xlsx"
TELEGRAM_TOKEN = "SEU_TOKEN_DO_BOT"
CHAT_ID = "SEU_CHAT_ID"
bot = Bot(token=TELEGRAM_TOKEN)

# --- Inicialização ---
if os.path.exists(ARQUIVO_EXCEL):
    df = pd.read_excel(ARQUIVO_EXCEL)
else:
    df = pd.DataFrame(columns=["tipo", "categoria", "valor", "data", "conta"])

# Metas por categoria e conta
metas = {
    "alimentação": {"limite": 500, "conta": "corrente"},
    "lazer": {"limite": 300, "conta": "cartão"},
    "transporte": {"limite": 200, "conta": "corrente"}
}

# --- Funções ---
def salvar_dados():
    df.to_excel(ARQUIVO_EXCEL, index=False)
    messagebox.showinfo("Salvo", "Dados salvos em Excel!")

def registrar_transacao():
    tipo = simpledialog.askstring("Tipo", "Digite 'despesa' ou 'receita':").lower()
    if tipo not in ["despesa", "receita"]:
        messagebox.showerror("Erro", "Tipo inválido!")
        return
    try:
        valor = float(simpledialog.askstring("Valor", "Digite o valor:"))
    except:
        messagebox.showerror("Erro", "Valor inválido!")
        return
    categoria = simpledialog.askstring("Categoria", "Digite a categoria:")
    conta = simpledialog.askstring("Conta", "Digite a conta (corrente/cartão/poupança):").lower()
    data = simpledialog.askstring("Data", "Digite a data (AAAA-MM-DD) ou Enter para hoje:")
    if data == "" or data is None:
        data = datetime.today().strftime("%Y-%m-%d")
    
    global df
    df = pd.concat([df, pd.DataFrame([{
        "tipo": tipo,
        "categoria": categoria,
        "valor": valor,
        "data": data,
        "conta": conta
    }])], ignore_index=True)
    
    messagebox.showinfo("Registrado", "✅ Transação registrada!")
    alertas_telegram(categoria, conta)

def calcular_saldo(conta=None):
    df_filtrado = df if not conta else df[df["conta"]==conta]
    saldo = df_filtrado.apply(lambda x: x["valor"] if x["tipo"]=="receita" else -x["valor"], axis=1).sum()
    messagebox.showinfo("Saldo", f"Saldo: R${saldo:.2f}")

def relatorio_categoria(conta=None):
    df_filtrado = df if not conta else df[df["conta"]==conta]
    despesas = df_filtrado[df_filtrado["tipo"]=="despesa"]
    resumo = despesas.groupby("categoria")["valor"].sum()
    messagebox.showinfo("Relatório", str(resumo))
    return resumo

def gerar_grafico(conta=None):
    resumo = relatorio_categoria(conta)
    if resumo.empty:
        messagebox.showinfo("Gráfico", "Sem dados para gráfico.")
        return
    resumo.plot.pie(autopct="%1.1f%%", ylabel="")
    plt.title(f"Despesas por Categoria{' - ' + conta if conta else ''}")
    plt.show()

def relatorio_mensal(conta=None):
    df_filtrado = df if not conta else df[df["conta"]==conta]
    df_filtrado["mes"] = pd.to_datetime(df_filtrado["data"]).dt.to_period("M")
    resumo = df_filtrado.groupby(["mes", "tipo"])["valor"].sum().unstack(fill_value=0)
    resumo["saldo"] = resumo.get("receita",0) - resumo.get("despesa",0)
    messagebox.showinfo("Resumo Mensal", str(resumo))
    resumo.plot(kind="bar", stacked=True)
    plt.title(f"Resumo Mensal{' - ' + conta if conta else ''}")
    plt.ylabel("Valor (R$)")
    plt.show()

def alertas_telegram(categoria, conta):
    if categoria.lower() in metas:
        meta = metas[categoria.lower()]
        if meta["conta"] != conta.lower():
            return
        gasto = df[(df["categoria"].str.lower()==categoria.lower()) & 
                   (df["tipo"]=="despesa") & 
                   (df["conta"]==conta.lower())]["valor"].sum()
        limite = meta["limite"]
        if gasto > limite:
            mensagem = f"⚠️ Alerta! Você ultrapassou o limite da categoria '{categoria}' na conta '{conta}'.\nGasto: R${gasto:.2f} | Limite: R${limite:.2f}"
            messagebox.showwarning("Alerta", mensagem)
            try:
                bot.send_message(chat_id=CHAT_ID, text=mensagem)
            except:
                print("Falha ao enviar alerta via Telegram")

# --- Interface gráfica ---
root = Tk()
root.title("Controle Financeiro Profissional")

Button(root, text="Registrar Transação", width=30, command=registrar_transacao).pack(pady=5)
Button(root, text="Ver Saldo", width=30, command=calcular_saldo).pack(pady=5)
Button(root, text="Relatório por Categoria", width=30, command=relatorio_categoria).pack(pady=5)
Button(root, text="Gráfico de Despesas", width=30, command=gerar_grafico).pack(pady=5)
Button(root, text="Resumo Mensal", width=30, command=relatorio_mensal).pack(pady=5)
Button(root, text="Salvar Dados", width=30, command=salvar_dados).pack(pady=5)
Button(root, text="Sair", width=30, command=root.quit).pack(pady=5)

root.mainloop()


