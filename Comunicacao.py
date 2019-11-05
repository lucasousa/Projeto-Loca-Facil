import socket 
import time
from skimage.io import imsave, imshow, imread
import pickle

class Conex():
	def __init__(self, ip, port):
		self.host = ip
		self.port = port
		
	def startConnection(self):
		self.address=((self.host,self.port))
		self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
		self.client_socket.connect(self.address)

	def sendMessage(self,content):	
		self.client_socket.send(content) 
	
	def receiveMessage(self):
		return pickle.loads(self.client_socket.recv(6144))

	def closeConnection(self):
		self.client_socket.close()