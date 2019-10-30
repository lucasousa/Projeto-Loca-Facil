import threading
import socket
from ast import literal_eval
from hashlib import md5
from database import DataBase


class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("Nova conexao: ", clientAddress)
        self.db = DataBase()
        

    def run(self):
        ack = None
        while True:
            packet = self.csocket.recv(6144).decode() 
            try:
                packet = literal_eval(packet)
                print(packet)
                if(self.defineOP(packet)):
                    ack = 1
                break
            except:
                pass
        message = {
            'status': 'success' if ack is not None else 'error'
        }
        print(message)
        self.csocket.send(str(message).encode())
        self.csocket.close()
    
    def defineOP(self, dic):
        if(dic['op'] == 'VerifyCadUser'):
            self.db.connect()
            busca = self.db.select("usuario", "user", "usuario='{}'".format(dic['usuario']))
            self.db.disconnect()
            print(busca)
            if(len(busca)==0):
                return True
            else:
                return False
        elif(dic['op'] == 'CadUser'):
            try:
                self.db.connect()
                """ self.db.insert_user(dic) """
                return True
            except:
                return False
        elif (dic['op'] == 'CadImovel'):
            try:
                self.db.connect()
                self.db.insert_rent(dic)
                self.db.disconnect()
                return True
            except:
                return False
        elif (dic['op'] == 'Login'):
            self.db.connect()
            verificador = self.db.select("senha", "user", "usuario='{}'".format(dic['login']))
            print(verificador[0]['senha'])
            print(self.db.crypt(dic['senha']))
            if(verificador[0]['senha'] == self.db.crypt(dic['senha'])):
                return True
            else:
                return False
            self.db.disconnect()
        
        else:
            pass #Contato
    
    def verificaLogin(self, dic):
        self.db.connect()
        verificador = self.db.select("senha", "user", "usuario='{}'".format(dic['usuario']))
        print(verificador)
        print(self.db.crypt(dic['senha']))
        if(verificador[0]['senha'] == self.db.crypt(dic['senha'])):
            return True
        else:
            return False
        self.db.disconnect()

if __name__ == '__main__':
    print()
    addr = ("", 7000)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(addr)
    print("Servidor iniciado!")
    print("Aguardando nova conexao..")
    while True:
        server.listen(10)
        clientsock, clientAddress = server.accept()
        newthread = ClientThread(clientAddress, clientsock)
        newthread.start()


""" 
class Servidor():
    def __init__(self):
        host = 'localhost'  #Não possui IP pois é local
        port = 7001
        addr = (host, port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria o socket
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reiniciliza o socket
        self.socket.bind(addr) #define a porta e quais ips podem se conectar com o servidor
        self.socket.listen(100)
        while(True):
            self.socket.accept()
            print("Nova conexão")
            user_thread = threading.Thread(target = receptor(self.socket))
            user_thread.start()
            user_thread.join()

def processador(mensagem):
    dado = literal_eval(mensagem)   #dicionário com o dado
    print(dado)
    #Gravar no banco

def receptor(socket):
    mensagem = socket.recv(1024).decode()
    processador = threading.Thread(target=processador(mensagem))
    processador.start()
    processador.join()


def aceitar(self):       
    while True:
        self.socket.accept()
        print("Nova Conexão")

Servidor() """
