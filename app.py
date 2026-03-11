from analise_vendas import dashboard_vendas
from conectar_banco import conectar
conexao = conectar()
dashboard_vendas(conexao)
import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
st.title("Dashboard de analise de vendas")
st.write("Projeto de analise de vendas utilizando Python,SQL e visualizacao de dados.")

query_kpi = """
    SELECT 
	SUM(vendas.quantidade * produtos.preco) AS faturamento_total,
    COUNT(vendas.id_venda) AS total_vendas,
    SUM(vendas.quantidade * produtos.preco) /
    COUNT(vendas.id_venda) AS ticket_medio
    from vendas
    join produtos
    ON vendas.id_produto = produtos.id_produto
    """
df_kpi = pd.read_sql(query_kpi, conexao)
faturamento_total = df_kpi["faturamento_total"][0]
total_vendas = df_kpi["total_vendas"][0]
ticket_medio = df_kpi["ticket_medio"][0]

print("\n===== KPI DE VENDAS =====")

print(f"Faturamento Total: R$ {faturamento_total:.2f}")
print(f"Total de Vendas: {total_vendas}")
print(f"Ticket Médio: R$ {ticket_medio:.2f}")

col1, col2, col3 = st.columns(3)

col1.metric("Faturamento Total", f"R$ {faturamento_total:.2f}")
col2.metric("Total de Vendas", total_vendas)
col3.metric("Ticket Médio", f"R$ {ticket_medio:.2f}")

fig_faturamento_total, ax = plt.subplots()
ax.bar(df_kpi["faturamento_total"], df_kpi["faturamento_total"], color = "steelblue")
plt.xticks(rotation = 45)
st.pyplot(fig_faturamento_total)















