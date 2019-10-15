import threading
import socket
from ast import literal_eval


class Servidor():
    pode_receber = True
    mensagem = None
    def __init__(self):
        host = ''  #Não possui IP pois é local
        port = 7000
        addr = (host, port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria o socket
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reiniciliza o socket
        self.socket.bind(addr) #define a porta e quais ips podem se conectar com o servidor
        self.socket.listen(100) #define o limite de conexoes
        threading.Thread(target = self.aceitar)
        threading.Thread(target = self.receptor)
        threading.Thread(target = self.Processador)

    def receptor(self):
        while True:
            if Servidor.pode_receber: 
                Servidor.mensagem = self.socket.recv(2048).decode()
                Servidor.pode_receber = False # Bloqueia a recepção

    def Processador(self):
        while True:
            if not Servidor.pode_receber:                #se existe uma mensagem
                dado = literal_eval(Servidor.mensagem)   #dicionário com o dado
                Servidor.mensagem = None
                Servidor.pode_receber = True             #pode receber novamente
                #Gravar no banco

    def aceitar(self):       
        while True:
            self.socket.accept()
            print("Nova conexão")

Servidor()

'''
import socket, threading
class ClientThread(threading.Thread):
    
    client_list = {}

    def _init_(self,clientAddress,clientsocket):
        threading.Thread._init_(self)
        self.csocket = clientsocket
        print ("Nova conexao: ", clientAddress)
        self.clientName = None
         
        
    def run(self):
        print ("Conectado de: ", clientAddress)
        msg = ''
        name = "Digite o seu nome >> "
        self.csocket.send(name.encode()) 
        self.clientName = self.csocket.recv(1024).decode()
        ClientThread.client_list[self.clientName]= self.csocket
        while True:
            data = self.csocket.recv(1024)
            msg = data.decode()
            
            if msg=='bye':
              break

            print ("from client", msg)
            
            for i,j in ClientThread.client_list.items():
                if(i != self.clientName):
                    j.send((self.clientName + ':' + ' ' + msg).encode()) 
        
        self.csocket.send(msg.encode())
        print ("Client at ", clientAddress,',', self.clientName,',', " disconnected...")


if _name_ == '_main_':
    LOCALHOST = ''
    PORT = 7000
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((LOCALHOST, PORT))
    print("Servidor iniciado!")
    print("Aguardando nova conexao..")
    while True:
        server.listen(1)
        clientsock, clientAddress = server.accept()
        newthread = ClientThread(clientAddress, clientsock)
        newthread.start()

'''