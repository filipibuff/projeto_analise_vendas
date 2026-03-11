from analise_vendas import dashboard_vendas
from conectar_banco import conectar
#from analise_vendas import analise_vendas
conexao = conectar()
dashboard_vendas(conexao)
#analise_vendas(conexao)

