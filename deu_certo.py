import pymysql

conexao = pymysql.connect(host = 'localhost', db='locafacil', user='root', passwd='lucas12')
cursor = conexao.cursor()



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

cursor.execute(sql)

sql = """ CREATE TABLE IF NOT EXISTS rent(
  idrent integer AUTO_INCREMENT,
  descricao VARCHAR(200) NULL,
  bairro VARCHAR(45) NOT NULL,
  situacao TINYINT NOT NULL,
  rua VARCHAR(45) NOT NULL,
  numero INT NOT NULL,
  complemento VARCHAR(45) NULL,
  cep VARCHAR(7) NOT NULL,
  preco FLOAT NOT NULL,
  qualidade FLOAT NOT NULL,
  id_user INT NOT NULL,
  PRIMARY KEY (idrent, id_user),
  CONSTRAINT id_user
    FOREIGN KEY (id_user)
    REFERENCES user(iduser)
    ON DELETE CASCADE
    ON UPDATE NO ACTION) """

cursor.execute(sql)

sql = """CREATE TABLE IF NOT EXISTS images(
  origem VARCHAR(200) NOT NULL,
  id_rent INT NOT NULL,
  PRIMARY KEY (id_rent),
  CONSTRAINT id_rent
    FOREIGN KEY (id_rent)
    REFERENCES rent (idrent)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)"""

cursor.execute(sql)

dic = dict()

dic['nome'] = "Lucas Sousa"
dic['cpf'] = "12345678910"
dic['telefone'] = "89999329025"
dic['email'] = "lucas@gmail.com"
dic['sexo'] = "masculino"
dic['usuario'] = "lucasousa"
dic['senha'] = "lucas12"

cursor.execute( 'INSERT INTO user( nome, cpf, telefone, email, sexo, usuario, senha ) VALUES (%s, %s, %s, %s, %s, %s, %s)', (  dic['nome'], dic['cpf'], dic['telefone'], dic['email'], dic['sexo'], dic['usuario'], dic['senha'] ))

cursor.execute('SELECT * from user')

for c in cursor:
    print(c)

conexao.commit()
conexao.close()
