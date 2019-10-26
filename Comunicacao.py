import socket 
import time
class Conex():
	def __init__(self, ip, port):
		self.host = ip
		self.port = port
		
	
	def startConnection(self):
		self.address=((self.host,self.port))
		self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
		self.client_socket.connect(self.address)

	def sendMessage(self,content):	
		self.client_socket.send(content.encode()) 
	
	def receiveMessage(self):
		return self.client_socket.recv(1024).decode()

	def closeConnection(self):
		self.client_socket.close()