# Escreva a função obter_colecao_mongodb(url_conexao, colecao) que irá se conectar no MogodDB utilizando alguma biblioteca do Python. Ela possui os seguintes parâmetros:
#    • url_conexao: URI de conexão com banco de dados MongoDB, que também informa a base de dados (database). Por exemplo: a URI `mongodb://localhost/bancoexemplo', é a string de conexão para o banco "bancoexemplo" da minha máquina local ("localhost").
#    • colecao: É o nome da coleção (collection) do MongoDB que estaremos acessando com esta função.
# Tempo estimado: 6 minutos. Dificuldade: quase média, a pessoa precisará lembrar como pegar o database ou da URI ou da própria biblioteca.

from pymongo import MongoClient

def obter_colecao_mongodb(url_conexao, colecao):
    db = MongoClient(url_conexão)
    col = db[colecao]
    return col

if __name__ == "__main__":
    url_conexao = "mongodb+srv://brunarnm:RdVVi5EFD4NmoTsO@cluster0.q3hewkz.mongodb.net/test"
    colecao = "produtos"
    ex = obter_colecao_mongodb(url_conexao, colecao)
    print(ex)