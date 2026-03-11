import matplotlib.pyplot as plt
import pandas as pd
from conectar_banco import conectar
def analise_vendas():

    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        query = """
        SELECT SUM(v.quantidade * p.preco) AS faturamento_total
        FROM vendas v
        JOIN produtos p ON v.id_produto = p.id_produto
        """

        cursor.execute(query)

        resultado = cursor.fetchone()

        print("Faturamento total:", resultado[0])

        #cursor.close()
        #conexao.close()

        query = """
        SELECT COUNT(*)
        FROM vendas
        """
        cursor.execute(query)

        resultado = cursor.fetchone()

        print("total de vendas:", resultado[0])

        query = """
        SELECT 
        SUM(v.quantidade * p.preco) / COUNT(v.id_venda) AS ticket_medio
        FROM vendas v
        JOIN produtos p ON v.id_produto = p.id_produto
        """
        cursor.execute(query)
        resultado = cursor.fetchone()

        print("Ticket médio:", resultado[0])

        query_nome = """
        SELECT 
        clientes.nome,
        SUM(vendas.quantidade * produtos.preco) AS faturamento_clientes
        from vendas
        join clientes
        ON vendas.id_clientes = clientes.id_clientes
        join produtos
        ON vendas.id_produto = produtos.id_produto
        GROUP BY clientes.nome
        ORDER BY faturamento_clientes DESC
        """
        df_nome = pd.read_sql(query_nome, conexao)
        print("clientes que geraram mais faturamento.")
        print(df_nome)	#pandas
        plt.figure(figsize=(10,6))
        plt.bar(df_nome["nome"], df_nome["faturamento_clientes"])
        plt.title("faturamento por cliente")
        plt.xlabel("nome")
        plt.ylabel("faturamento R$")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        

        
        

        query_produtos = """
        SELECT produtos.nome_produto,
        SUM(vendas.quantidade) AS total_vendido
        from vendas
        join produtos
        ON vendas.id_produto = produtos.id_produto
        GROUP BY produtos.nome_produto
        ORDER BY total_vendido DESC
        """
        
        

        df_produtos = pd.read_sql(query_produtos, conexao)
        print("\nprodutos mais vendidos.")
        print(df_produtos)	#pandas
        plt.figure(figsize=(10,6))
        plt.bar(df_produtos["nome_produto"], df_produtos["total_vendido"])
        plt.title("produtos mais vendidos")
        plt.xlabel("produto")
        plt.ylabel("quantidade vendida")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
         
        query_faturamentoprodutos = """
        SELECT 
        produtos.nome_produto,
        SUM(vendas.quantidade * produtos.preco) AS faturamento_produto
        from vendas
        join produtos
        ON vendas.id_produto = produtos.id_produto
        GROUP BY produtos.nome_produto
        ORDER BY faturamento_produto DESC
        """
        df_faturamentoprodutos = pd.read_sql(query_faturamentoprodutos, conexao)
        print(df_faturamentoprodutos)

        print("\nfaturamento por produto.")
        print(df_faturamentoprodutos)	#pandas
        plt.figure(figsize=(10,6))
        plt.bar(df_faturamentoprodutos["nome_produto"], df_faturamentoprodutos["faturamento_produto"])
        plt.title("faturamento por produto")
        plt.xlabel("produto")
        plt.ylabel("faturamento (R$)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
           




        query_vendas_trimestre = """
        SELECT 
        MONTH(vendas.data_venda) AS mes,
        SUM(vendas.quantidade * produtos.preco) AS faturamento
        from vendas
        join produtos
        ON vendas.id_produto = produtos.id_produto
        GROUP BY  mes
        ORDER BY mes
        """
        df_vendas_trimestre = pd.read_sql(query_vendas_trimestre, conexao)
        print("\nvendas por trimestre.")
        print(df_vendas_trimestre)	#pandas
        plt.figure(figsize=(10,6))
        plt.bar(df_vendas_trimestre["mes"], df_vendas_trimestre["faturamento"])
        plt.title("faturamento por epoca")
        plt.xlabel("trimestre")
        plt.ylabel("faturamento (R$)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


        query = """
        SELECT clientes.nome,
        SUM(vendas.quantidade) AS total_comprado
        from vendas
        join clientes
        on vendas.id_clientes = clientes.id_clientes
        GROUP BY clientes.nome
        ORDER BY total_comprado DESC
        """
        cursor.execute(query)
        resultado = cursor.fetchall()
        print("\ntotal comprado por clientes:")
        
        for cliente, quantidade in resultado:
            print(f"cliente: {cliente} | quantidade:  {quantidade}")
        

        
        cursor.close()
        conexao.close()

        print("ate logo!")


def grafico_clientes(conexao):
    query_nome = """
    SELECT 
    clientes.nome,
    SUM(vendas.quantidade * produtos.preco) AS faturamento_clientes
    from vendas
    join clientes
    ON vendas.id_clientes = clientes.id_clientes
    join produtos
    ON vendas.id_produto = produtos.id_produto
    GROUP BY clientes.nome
    ORDER BY faturamento_clientes DESC
    """
    df_nome = pd.read_sql(query_nome, conexao)
    print("clientes que geraram mais faturamento.")
    print(df_nome)	#pandas
    plt.figure(figsize=(10,6))
    plt.bar(df_nome["nome"], df_nome["faturamento_clientes"])
    plt.title("faturamento por cliente")
    plt.xlabel("nome")
    plt.ylabel("faturamento R$")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    
def grafico_produtos(conexao):
    query_produtos = """
    SELECT produtos.nome_produto,
    SUM(vendas.quantidade) AS total_vendido
    from vendas
    join produtos
    ON vendas.id_produto = produtos.id_produto
    GROUP BY produtos.nome_produto
    ORDER BY total_vendido DESC
    """
        
        

    df_produtos = pd.read_sql(query_produtos, conexao)
    print("\nprodutos mais vendidos.")
    print(df_produtos)	#pandas
    plt.figure(figsize=(10,6))
    plt.bar(df_produtos["nome_produto"], df_produtos["total_vendido"])
    plt.title("produtos mais vendidos")
    plt.xlabel("produto")
    plt.ylabel("quantidade vendida")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
def grafico_faturamentoprodutos(conexao):
    query_faturamentoprodutos = """
    SELECT 
    produtos.nome_produto,
    SUM(vendas.quantidade * produtos.preco) AS faturamento_produto
    from vendas
    join produtos
    ON vendas.id_produto = produtos.id_produto
    GROUP BY produtos.nome_produto
    ORDER BY faturamento_produto DESC
    """
    df_faturamentoprodutos = pd.read_sql(query_faturamentoprodutos, conexao)
    print(df_faturamentoprodutos)

    print("\nfaturamento por produto.")
    print(df_faturamentoprodutos)	#pandas
    plt.figure(figsize=(10,6))
    plt.bar(df_faturamentoprodutos["nome_produto"], df_faturamentoprodutos["faturamento_produto"])
    plt.title("faturamento por produto")
    plt.xlabel("produto")
    plt.ylabel("faturamento (R$)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def grafico_vendas_trimestre(conexao):
    query_vendas_trimestre = """
    SELECT 
    MONTH(vendas.data_venda) AS mes,
    SUM(vendas.quantidade * produtos.preco) AS faturamento
    from vendas
    join produtos
    ON vendas.id_produto = produtos.id_produto
    GROUP BY  mes
    ORDER BY mes
    """
    df_vendas_trimestre = pd.read_sql(query_vendas_trimestre, conexao)
    print("\nvendas por trimestre.")
    print(df_vendas_trimestre)	#pandas
    plt.figure(figsize=(10,6))
    plt.bar(df_vendas_trimestre["mes"], df_vendas_trimestre["faturamento"])
    plt.title("faturamento por epoca")
    plt.xlabel("trimestre")
    plt.ylabel("faturamento (R$)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()






def analise_vendas(conexao):
    print("Iniciando Analise")
    grafico_clientes(conexao)
    grafico_produtos(conexao)
    grafico_faturamentoprodutos(conexao)
    grafico_vendas_trimestre(conexao)
    print("\nAnalise finalizada.")

def dashboard_vendas(conexao):

    fig, axs = plt.subplots(2,2, figsize=(14,10))
    # top clientes
    query_nome = """
    SELECT 
    clientes.nome,
    SUM(vendas.quantidade * produtos.preco) AS faturamento_clientes
    from vendas
    join clientes
    ON vendas.id_clientes = clientes.id_clientes
    join produtos
    ON vendas.id_produto = produtos.id_produto
    GROUP BY clientes.nome
    ORDER BY faturamento_clientes DESC
    """
    df_nome = pd.read_sql(query_nome, conexao)
    axs[0,0].bar(df_nome["nome"], df_nome["faturamento_clientes"])
    axs[0,0].set_title("top clientes")
    axs[0,0].tick_params(axis = "x", rotation = 45)

    # produtos mais vendidos
    query_produtos = """
    SELECT produtos.nome_produto,
    SUM(vendas.quantidade) AS total_vendido
    from vendas
    join produtos
    ON vendas.id_produto = produtos.id_produto
    GROUP BY produtos.nome_produto
    ORDER BY total_vendido DESC
    """
    df_produtos = pd.read_sql(query_produtos, conexao)
    axs[0,1].bar(df_produtos["nome_produto"], df_produtos["total_vendido"])
    axs[0,1].set_title("total vendindo")
    axs[0,1].tick_params(axis = "x", rotation = 45)

    #faturamento por produto
    query_faturamentoprodutos = """
    SELECT 
    produtos.nome_produto,
    SUM(vendas.quantidade * produtos.preco) AS faturamento_produto
    from vendas
    join produtos
    ON vendas.id_produto = produtos.id_produto
    GROUP BY produtos.nome_produto
    ORDER BY faturamento_produto DESC
    """
    df_faturamentoprodutos = pd.read_sql(query_faturamentoprodutos, conexao)
    axs[1,0].bar(df_faturamentoprodutos["nome_produto"], df_faturamentoprodutos["faturamento_produto"])
    axs[1,0].set_title("faturamento por produto")
    axs[1,0].tick_params(axis = "x", rotation = 45)

    #vendas trimestrais
    query_vendas_trimestre = """
    SELECT 
    MONTH(vendas.data_venda) AS mes,
    SUM(vendas.quantidade * produtos.preco) AS faturamento
    from vendas
    join produtos
    ON vendas.id_produto = produtos.id_produto
    GROUP BY  mes
    ORDER BY mes
    """
    df_vendas_trimestre = pd.read_sql(query_vendas_trimestre, conexao)
    axs[1,1].bar(df_vendas_trimestre["mes"], df_vendas_trimestre["faturamento"])
    axs[1,1].set_title("vendas trimestre")
    axs[1,1].tick_params(axis = "x", rotation = 45)

    axs[0,0].bar(df_nome["nome"], df_nome["faturamento_clientes"],color = "steelblue")
    axs[0,1].bar(df_produtos["nome_produto"], df_produtos["total_vendido"],color = "darkorange")
    axs[1,0].bar(df_faturamentoprodutos["nome_produto"], df_faturamentoprodutos["faturamento_produto"],color = "seagreen")
    axs[1,1].bar(df_vendas_trimestre["mes"], df_vendas_trimestre["faturamento"],color = "indianred")
    plt.tight_layout()
    plt.show()

    #trabalhar cores

    #KPI de vendas

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

    #formatacao para grafico pizza

    query_pizza = """
    SELECT 
	produtos.nome_produto,
    SUM(vendas.quantidade * produtos.preco) AS faturamento_produto
    from vendas
    join produtos
    ON vendas.id_produto = produtos.id_produto
    GROUP BY produtos.nome_produto
    """
    df_pizza = pd.read_sql(query_pizza, conexao)
    #grafico pizza
    fig, ax = plt.subplots(figsize=(8,8))

    wedges, texts, autotexts = ax.pie(
        df_pizza["faturamento_produto"],
        autopct="%1.1f%%",
        startangle=60
    )

    ax.legend(
        wedges,
        df_pizza["nome_produto"],
        title="Produtos",
        loc="center left",
        bbox_to_anchor=(1, 0, 0.5, 1)
    )

    ax.set_title("Participação de Faturamento por Produto")

    plt.show()
    
        
   
     

    
    
    
   
    
    
    
    
    
    
    
    
    
    
    