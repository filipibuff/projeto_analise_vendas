import mysql.connector

def conectar():

    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="filipi",
            password="1234",
            database="analise_vendas"
        )

        print("Conexão realizada com sucesso")
        return conexao

    except mysql.connector.Error as erro:
        print("Erro ao conectar:", erro)
        return None