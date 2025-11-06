import pandas as pd
from datetime import datetime

# Dados de exemplo
dados = {
    "Data": [
        datetime(2025, 11, 1),
        datetime(2025, 11, 3),
        datetime(2025, 11, 5),
        datetime(2025, 11, 6)
    ],
    "Descrição": [
        "Salário",
        "Supermercado",
        "Aluguel",
        "Transporte"
    ],
    "Categoria": [
        "Receita",
        "Despesa",
        "Despesa",
        "Despesa"
    ],
    "Valor (R$)": [
        5000,
        -350,
        -1200,
        -200
    ]
}

# Cria o DataFrame
df = pd.DataFrame(dados)

# Calcula o saldo final
saldo_final = df["Valor (R$)"].sum()

# Adiciona uma linha com o saldo total
df.loc[len(df)] = ["", "Saldo final", "", saldo_final]

# Salva como Excel
arquivo = "planejamento_financeiro.xlsx"
df.to_excel(arquivo, index=False, engine="openpyxl")

print(f"✅ Planilha '{arquivo}' criada com sucesso!")

