import pymysql
from hashlib import md5

class DataBase(object):
    def __init__(self):
        self.host = 'localhost'
        self.usuario = 'root'
        self.db = 'locafacil'
        self.password = 'samuel123'
        self.port = 8001
        self.conexao = None
        self.cursor = None

    def crypt(self, string):
        return md5(string.encode()).hexdigest()

    def connect(self):
        self.conexao = pymysql.connect(host=self.host, db=self.db, user=self.usuario,port = self.port, passwd=self.password)
        self.cursor = self.conexao.cursor(pymysql.cursors.DictCursor) # Os resultados vem em dicionario

    def disconnect(self):
        self.conexao.close()

    def select(self, fields, tables, where=None):
        query = "SELECT " + fields + " FROM " + tables

        if(where):
            query = query + " WHERE " + where
        print('query: ', query)
        self.cursor.execute(query)
        return self.cursor.fetchall() #pega todos os resultados da execução acima e retorna
        
    def insert_user(self, dic):
        if(self.select("cpf","user","cpf = {}".format(dic['cpf']))):
            pass
        else:
            self.cursor.execute ('INSERT INTO user( nome, cpf, telefone, email, sexo, usuario, senha ) VALUES (%s, %s, %s, %s, %s, %s, %s)',(  dic['nome'], dic['cpf'], dic['telefone'], dic['email'], dic['sexo'], dic['usuario'], self.crypt(dic['senha']) ))

        self.conexao.commit()
    
    def insert_rent(self, dic):
        dic['id_user'] = self.select('iduser','user', "cpf = '{}'".format(dic['id_user']))[0]['iduser']
        print(dic)
        self.cursor.execute ('INSERT INTO rent(descricao, bairro, situacao, rua, numero, complemento, cep, preco, id_user ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)', (dic['desc'], dic['bairro'], dic['sit'], dic['rua'], int(dic['numero']), dic['complemento'], dic['cep'], float(dic['preco']), int(dic['id_user'])))
        self.conexao.commit()

    def update(self, dic, table, where=None): #dic vai ser um dicionário (field = value)
        query = "UPDATE " + table
        query = query + " SET " + ",".join([field + " = '" + value + "'" for field, value in dic.items()])
        
        if(where):
            query = query + " WHERE " + where

        self.cursor.execute(query)
        self.conexao.commit()
    

    def create_tables(self):
        sql = """ CREATE TABLE IF NOT EXISTS user(
        iduser integer AUTO_INCREMENT,
        nome text NOT NULL,
        cpf VARCHAR(11) NOT NULL,
        telefone VARCHAR(11) NOT NULL,
        email VARCHAR(45) NOT NULL,
        sexo VARCHAR(9) NOT NULL,
        usuario VARCHAR(20) NOT NULL,
        senha VARCHAR(32) NOT NULL,
        PRIMARY KEY (iduser, cpf) )"""
        self.cursor.execute(sql)

        sql = """ CREATE TABLE IF NOT EXISTS rent(
        idrent integer AUTO_INCREMENT,
        descricao VARCHAR(200) NULL,
        bairro VARCHAR(45) NOT NULL,
        situacao TINYINT NOT NULL,
        rua VARCHAR(45) NOT NULL,
        numero INT NOT NULL,
        complemento VARCHAR(45) NULL,
        cep VARCHAR(8) NOT NULL,
        preco FLOAT NOT NULL,
        id_user INT NOT NULL,
        PRIMARY KEY (idrent, id_user),
        CONSTRAINT id_user
            FOREIGN KEY (id_user)
            REFERENCES user(iduser)
            ON DELETE CASCADE
            ON UPDATE NO ACTION) """
        self.cursor.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS images(
        origem VARCHAR(200) NOT NULL,
        id_rent INT NOT NULL,
        PRIMARY KEY (id_rent),
        CONSTRAINT id_rent
            FOREIGN KEY (id_rent)
            REFERENCES rent (idrent)
            ON DELETE CASCADE
            ON UPDATE NO ACTION)"""
        self.cursor.execute(sql)


if __name__ == '__main__':

    data = DataBase()
    data.connect()


    #--------- Deu certo ----------------
    a = data.select("nome, cpf", "user", "iduser = 759347639")
    print(a)
    a = data.select("nome, cpf", "user")
    print(a)
    #-------------------------------------

    dic = dict()

    dic['nome'] = "Sousa"
    dic['cpf'] = "12345678911"
    dic['telefone'] = "89999329025"
    dic['email'] = "lucas@gmail.com"
    dic['sexo'] = "masculino"
    dic['usuario'] = "lucas"
    dic['senha'] = "lucasous"

    #--------- Deu certo ----------------
    data.insert_user(dic)
    #-------------------------------------


    dicio= dict()
    dicio['desc'] = "Pais Tropical"
    dicio['bairro'] = "Junco"
    dicio['sit'] = 1
    dicio['rua'] = "Avenida Piauí"
    dicio['numero'] = 338
    dicio['complemento'] = "Em frente a Igreja São Francisco"
    dicio['cep'] = "6460784"
    dicio['preco'] = 500.00
    dicio['id_user'] = 1

    #--------- Deu certo ----------------
    data.insert_rent(dicio)
    #-------------------------------------

    data.update({'senha': '@naosei123'}, "user", "iduser = 1")

    data.disconnect()