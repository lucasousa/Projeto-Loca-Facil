class Cliente():

    def __init__(self, nome, cpf, endereco, cep, telefone):
        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = endereco
        self.__cep = cep
        self.__telefone = telefone

    def getNome(self):
        return self.__nome

    def getEndereco(self):
        return self.__endereco

    def getCep(self):
        return self.__cep

    def getTelefone(self):
        return self.__telefone

    def getCpf(self):
        return self.__cpf

    def setNome(self, nome):
        self.__nome = nome

    def setEndereco(self, endereco):
        self.__endereco = endereco

    def setCep(self, cep):
        self.__cep = cep

    def setTelefone(self, telefone):
        self.__telefone = telefone

    def setCpf(self, cpf):
        self.__cpf = cpf

    nome = property(getNome,setNome)
    endereco = property(getEndereco,setEndereco)
    cep = property(getCep,setCep)
    telefone = property(getTelefone,setTelefone)
    cpf = property(getCpf,setCpf)

class Cadastro():

    def __init__(self):
        self.__clientes = []
        self.__total_cliente = 0

    def cadastra(self, cliente):
        self.__clientes.append(cliente)
        self.__total_cliente += 1

    def getTotal(self):
        return self.__total_cliente

    def verifica_cadastro(self, teste_cpf):
        if self.__total_cliente == 0:
            return True

        for cliente in self.__clientes:
            if cliente.cpf == teste_cpf:
                return False
        return True

'''
cl1 = Cliente('Romuere','Picos', '64000000','86999999999','00000000000')
cd = Cadastro()
cd.cadastra(cl1)
print(cd.verifica_cadastro('00000000000'))
'''
