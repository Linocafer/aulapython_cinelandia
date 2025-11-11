import pandas as pd

# --- Dados de exemplo ---
dados = {
    "Data": ["01/11/2025", "03/11/2025", "05/11/2025", "06/11/2025"],
    "Descrição": ["Salário", "Supermercado", "Aluguel", "Transporte"],
    "Categoria": ["Receita", "Despesa", "Despesa", "Despesa"],
    "Valor (R$)": [5000, -350, -1200, -200]
}

df = pd.DataFrame(dados)

# --- Calcula saldo e totais ---
total_receitas = df[df["Valor (R$)"] > 0]["Valor (R$)"].sum()
total_despesas = df[df["Valor (R$)"] < 0]["Valor (R$)"].sum()
saldo = total_receitas + total_despesas

# Adiciona linha de resumo
resumo = pd.DataFrame({
    "Data": [""],
    "Descrição": ["Resumo"],
    "Categoria": [""],
    "Valor (R$)": [saldo]
})
df_final = pd.concat([df, resumo], ignore_index=True)

# --- Salvar Excel com formatação usando xlsxwriter ---
arquivo = "Orcamento_Pessoal.xlsx"
writer = pd.ExcelWriter(arquivo, engine="xlsxwriter")
df_final.to_excel(writer, index=False, sheet_name="Orçamento")

workbook = writer.book
worksheet = writer.sheets["Orçamento"]

# Formatação de cabeçalho
cabecalho_format = workbook.add_format({
    "bold": True,
    "text_wrap": True,
    "valign": "center",
    "fg_color": "#4CAF50",
    "font_color": "white",
    "border": 1
})
for col_num, value in enumerate(df_final.columns.values):
    worksheet.write(0, col_num, value, cabecalho_format)

# Formatação de células
receita_format = workbook.add_format({"bg_color": "#C6EFCE", "font_color": "#006100"})
despesa_format = workbook.add_format({"bg_color": "#FFC7CE", "font_color": "#9C0006"})
resumo_format = workbook.add_format({"bold": True, "bg_color": "#FFEB9C", "border": 1})

for row_num, valor in enumerate(df_final["Valor (R$)"], start=1):
    if row_num == len(df_final):  # última linha (resumo)
        worksheet.write(row_num, 3, valor, resumo_format)
    elif valor > 0:
        worksheet.write(row_num, 3, valor, receita_format)
    else:
        worksheet.write(row_num, 3, valor, despesa_format)

# Ajustar largura das colunas
worksheet.set_column("A:A", 12)
worksheet.set_column("B:B", 25)
worksheet.set_column("C:C", 12)
worksheet.set_column("D:D", 12)

# --- Adicionar gráfico de pizza das despesas ---
chart = workbook.add_chart({"type": "pie"})

# Filtra despesas
despesas = df_final[df_final["Valor (R$)"] < 0].copy()
despesas["Valor (R$)"] = despesas["Valor (R$)"].abs()

# Adiciona dados do gráfico
worksheet_chart_start_row = len(df_final) + 2
chart.add_series({
    "name": "Distribuição de Despesas",
    "categories": [f"Orçamento", 1, 1, len(despesas), 1],
    "values":     [f"Orçamento", 1, 3, len(despesas), 3],
    "data_labels": {"percentage": True}
})

chart.set_title({"name": "Despesas por Categoria"})
worksheet.insert_chart(f"B{worksheet_chart_start_row}", chart, {"x_scale": 1.5, "y_scale": 1.5})

# Salvar arquivo
writer.close()
print(f"✅ Planilha '{arquivo}' criada com sucesso!")
