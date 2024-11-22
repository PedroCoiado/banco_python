# importar o drive de comunicação do Python com o MySQL
import mysql.connector as mc

# Vamos criar uma função para estabelecer a conexão com o banco de dados
# todas as vezes que for executar uma consulta em uma das tabelas, esta
# função pode ser utilizada
def conectar_banco():
    banco = mc.connect(
        host="127.0.0.1",
        port=3307,
        user="root",
        password="",
        database="locadora"        
    )
    cursor = banco.cursor()
    return banco,cursor 

