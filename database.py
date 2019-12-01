import pymysql
from hashlib import md5

class DataBase(object):
    """   
   Esta classe tem por objetivo fazer a conexão com banco de dados e realizar operaçãos (CRUD) no mesmo 

    ...

    Atributos
    ----------
    host : str
        representa o host a qual esta rodando o banco de dados, nesse caso na máquina local
    usuario : str
        define o usuário a qual terá acesso para manipular o banco de dados
    db : str
        banco de dados a qual será realizadas as operações
    password : str
        senha de acesso ao banco de dados
    conexao : objeto
        Objeto pelo qual será responsável por estabelecer a conexão, salvar arquivos e fechar banco de dados
    cursor : objeto
        objeto que será responsável por executar operações no banco, tais como: execute(inserir dados em uma tabela)
    """
    def __init__(self):
        self.host = 'localhost'
        self.usuario = 'root'
        self.db = 'locafacil'
        self.password = 'lucas12'
        self.conexao = None
        self.cursor = None

    def crypt(self, string):
        """ 
        Este método objetiva criptografar uma senha (string normal) para o formato md5
        
        ...

        Parâmetros
        ----------
        string : str
            representa a senha que será codificada para o formato md5
        
        Returns
        -------
        str
            string no formato md5
        """
        return md5(string.encode()).hexdigest()

    def connect(self):
        """
        Este é o método onde é iniciada uma conexão com o banco de dados
        ...

        Parâmetros
        ---------
        self.conexao: objeto
            definido como objeto de acesso ao bd
        self.cursor: objeto
            definido como objeto para fazer manipulações com o bd, tais como: salvar, executar uma operação
        """
        self.conexao = pymysql.connect(host=self.host, db=self.db, user=self.usuario, passwd=self.password)
        self.cursor = self.conexao.cursor(pymysql.cursors.DictCursor) # Os resultados vem em dicionario

    def disconnect(self):
        """
        método para desfazer a conexão com o banco de dados, ou seja, fechar o mesmo
        """
        self.conexao.close()

    def select(self, fields, tables, where=None):
        """
        Método para fazer seleções(buscas) no banco de dados

        Parâmetros
        ----------
        fields : list
            são os campos ao qual quero selecionar na busca no banco de dados
        tables : str
            tabela a qual será feita a seleção
        if where : list
           representa uma ou mais condições para realizar a seleção, ex: buscar dados na tabela X onde primary_key == 1
        
        Returns
        -------
        dict   
            composto por todos os dados que satisfaz a seleção
        """
        query = "SELECT " + fields + " FROM " + tables

        if(where):
            query = query + " WHERE " + where
        print('query: ', query)
        self.cursor.execute(query)
        return self.cursor.fetchall() #pega todos os resultados da execução acima e retorna
        
    def insert_user(self, dic):
        """ 
        Este método faz a inserção de um usuário na tabela user no banco de dados

        ...

        Parâmetros
        ----------
        dic : dict
            Dicionário com os campos necessários para a inserção de um usuário no sistema
        """
        self.cursor.execute("INSERT INTO user( nome, cpf, telefone, email, sexo, usuario, senha ) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(  str(dic['nome']), str(dic['cpf']), str(dic['telefone']), str(dic['email']), str(dic['sexo']), str(dic['usuario']), self.crypt(dic['senha']) ))
        self.conexao.commit()

    def insert_image(self, dic):
        """ 
        Este método faz a inserção de uma imagem na tabela image no banco de dados

        ...

        Parâmetros
        ----------
        dic : dict
            Dicionário com os campos necessários para a inserção de uma imagem no sistema
        """
        self.cursor.execute("INSERT INTO images(origem, id_rent) VALUES ('{}',{})".format(dic['FileName'],dic['id']))
        self.conexao.commit()
    def insert_rent(self, dic):
        """ 
        Este método faz a inserção de um imóvel na tabela rent no banco de dados

        ...

        Parâmetros
        ----------
        dic : dict
            Dicionário com os campos necessários para a inserção de um imóvel no sistema
        """
        dic['id_user'] = self.select('iduser','user', "cpf = '{}'".format(dic['id_user']))[0]['iduser']
        self.cursor.execute("INSERT INTO rent(descricao, bairro, situacao, rua, numero, complemento, cep, preco, id_user ) VALUES ('{}','{}',{},'{}',{},'{}','{}',{},{})".format(dic['desc'], dic['bairro'], int(dic['sit']), dic['rua'], int(dic['numero']), dic['complemento'], dic['cep'], float(dic['preco']), int(dic['id_user'])))
        self.conexao.commit()

    def update(self, dic, table, where=None): #dic vai ser um dicionário (field = value)
        """ 
        Este método faz a atualização dos dados de uma tabela no banco de dados

        ...

        Parâmetros
        ----------
        dic : dict
            Dicionário com os campos a serem atualizados
        table : str
            tabela do banco de dados a qual será atualizada
        if where : list 
            condição para atualização da tabela, ou seja, será atualizado onde houver os campos presentes no where
        """
        query = "UPDATE " + table
        query = query + " SET " + ",".join([field + " = '" + value + "'" for field, value in dic.items()])
        
        if(where):
            query = query + " WHERE " + where

        self.cursor.execute(query)
        self.conexao.commit()
    
    def delete(self, table, where=None):
        """
        Método responsável por deletar campo(s) em uma tabela no banco de dados

        ...

        Parâmetros
        ----------
        table : str 
            tabela a qual serão deletados o(s) campo(s)
        if where : list
            onde os campos forem iguais os que estão presentes no parâmetro where
        else
            deletar todos campos da tabela
        """
        query = "DELETE FROM " + table
        
        if(where):
            query = query + " WHERE " + where

        self.cursor.execute(query)
        self.conexao.commit()
