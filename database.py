import pymysql
from hashlib import md5

class DataBase(object):
    def __init__(self):
        self.host = 'localhost'
        self.usuario = 'root'
        self.db = 'locafacil'
        self.password = 'samuel123'
        self.conexao = None
        self.cursor = None

    def crypt(self, string):
        return md5(string.encode()).hexdigest()

    def connect(self):
        self.conexao = pymysql.connect(host=self.host, db=self.db, user=self.usuario, passwd=self.password)
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
        self.cursor.execute("INSERT INTO user( nome, cpf, telefone, email, sexo, usuario, senha ) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(  str(dic['nome']), str(dic['cpf']), str(dic['telefone']), str(dic['email']), str(dic['sexo']), str(dic['usuario']), self.crypt(dic['senha']) ))
        self.conexao.commit()

    
    def insert_rent(self, dic):
        dic['id_user'] = self.select('iduser','user', "cpf = '{}'".format(dic['id_user']))[0]['iduser']
        self.cursor.execute("INSERT INTO rent(descricao, bairro, situacao, rua, numero, complemento, cep, preco, id_user ) VALUES ('{}','{}',{},'{}',{},'{}','{}',{},{})".format(dic['desc'], dic['bairro'], int(dic['sit']), dic['rua'], int(dic['numero']), dic['complemento'], dic['cep'], float(dic['preco']), int(dic['id_user'])))
        self.conexao.commit()

    def update(self, dic, table, where=None): #dic vai ser um dicionário (field = value)
        query = "UPDATE " + table
        query = query + " SET " + ",".join([field + " = '" + value + "'" for field, value in dic.items()])
        
        if(where):
            query = query + " WHERE " + where
        print(query)
        self.cursor.execute(query)
        self.conexao.commit()
    
    def delete(self, table, where=None):
        query = "DELETE FROM " + table
        
        if(where):
            query = query + " WHERE " + where

        self.cursor.execute(query)
        self.conexao.commit()
