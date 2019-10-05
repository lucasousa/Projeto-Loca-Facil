from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QTableWidgetItem
from Telas.telainicial import Ui_telainicial
from Telas.login import Ui_login
from Telas.maintela import Ui_maintela
from Telas.cadastroimovel import Ui_cadastroimovel
from Telas.cadastrousuario import Ui_cadastrousuario
from Telas.contato import Ui_contato
from Telas.recuperar_login import Ui_recuperar_login
from PyQt5.QtGui import QPixmap
import PyQt5
import sys
import os
from PyQt5.QtCore import pyqtSlot
from classes import Person, Rent, Renter, User
from Comunicacao import Conex
import threading
from ast import literal_eval

Users = []

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(1200, 900)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()

        self.tela_inicio = Ui_telainicial()
        self.tela_inicio.setupUi(self.stack0)

        self.tela_login = Ui_login()
        self.tela_login.setupUi(self.stack1)

        self.tela_principal = Ui_maintela()
        self.tela_principal.setupUi(self.stack2)

        self.tela_cadastro_usuario = Ui_cadastrousuario()
        self.tela_cadastro_usuario.setupUi(self.stack3)

        self.tela_cadastro_imovel = Ui_cadastroimovel()
        self.tela_cadastro_imovel.setupUi(self.stack4)

        self.tela_contato = Ui_contato()
        self.tela_contato.setupUi(self.stack5)

        self.tela_recuperar_login = Ui_recuperar_login()
        self.tela_recuperar_login.setupUi(self.stack6)

        self.QtStack.addWidget(self.stack0) #Tela inicial
        self.QtStack.addWidget(self.stack1) #Tela login
        self.QtStack.addWidget(self.stack2) #Tela principal
        self.QtStack.addWidget(self.stack3) #Tela Cadastro de Usuário
        self.QtStack.addWidget(self.stack4) #Tela Cadastro de Imóvel
        self.QtStack.addWidget(self.stack5) #Tela de contato
        self.QtStack.addWidget(self.stack6) #Tela de recuperar login


class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        # self.conexao = Conex() #Socket comentado
        super(Main, self).__init__(parent)
        self.setupUi(self)
        
        #Tela inicial
        self.tela_inicio.pushButton.clicked.connect(self.AbrirTelaCadUser) #Botão cadastrar
        self.tela_inicio.pushButton_2.clicked.connect(self.AbrirTelaLogin) #Botão Login
        #login
        self.tela_login.pushButton.clicked.connect(self.AbrirTelaPrincipal) #Botão Entrar 
        #Main tela
        self.tela_principal.toolButton.clicked.connect(self.AbrirTelaCadImovel) #Cadastrar Imóvel
        self.tela_principal.toolButton_3.clicked.connect(self.Erro) #Visualizar Imóveis
        self.tela_principal.toolButton_5.clicked.connect(self.Erro) #Sobre
        self.tela_principal.toolButton_4.clicked.connect(self.AbrirTelaContato) #Contato
    
        self.tela_contato.toolButton.clicked.connect(self.AbrirTelaPrincipal) #Botão voltar (tela principal)
        self.tela_login.toolButton.clicked.connect(self.AbrirTelaRecuperarLogin) #Link para recuperar Login

        #cadastro Usuário
        self.tela_cadastro_usuario.pushButton.clicked.connect(self.CadastrarUsuario) #Cadastrar
        #self.tela_cadastro_usuario.pushButton.clicked.connect(self.AbrirTelaPrincipal) #Cadastrar 
        #Cadastro Imóvel
        self.tela_cadastro_imovel.pushButton.clicked.connect(self.CadastrarImovel) #Cadastrar
    
    def Erro(self):
        QtWidgets.QMessageBox.about(None, "Erro","Função em desenvolvimento")

    
    def AbrirTelaInicial(self):
        self.QtStack.setCurrentIndex(0)
    def AbrirTelaLogin(self):
        self.QtStack.setCurrentIndex(1)
    def AbrirTelaPrincipal(self):
        self.QtStack.setCurrentIndex(2)
    def AbrirTelaCadUser(self):
        self.QtStack.setCurrentIndex(3)
    def AbrirTelaCadImovel(self):
        self.QtStack.setCurrentIndex(4)
    def AbrirTelaContato(self):
        self.QtStack.setCurrentIndex(5)
    def AbrirTelaRecuperarLogin(self):
        self.QtStack.setCurrentIndex(6)


    def CadastrarImovel(self):
        dicio = {}
        dicio['desc'] = self.tela_cadastro_imovel.lineEdit_10.text()
        dicio['bairro'] = self.tela_cadastro_imovel.lineEdit_5.text()
        dicio['rua'] = self.tela_cadastro_imovel.lineEdit_7.text()
        dicio['numero'] = self.tela_cadastro_imovel.lineEdit_9.text()
        dicio['complemento'] = self.tela_cadastro_imovel.lineEdit_8.text()
        dicio['cep'] = self.tela_cadastro_imovel.lineEdit_6.text()
        dicio['preço'] = self.tela_cadastro_imovel.lineEdit_5.text()
        dicio['cpf'] = self.tela_cadastro_imovel.lineEdit_12.text()
        #Guardando as informações da tela em um dicionário
        if():
            pass
        #verificações para o cadastro

    def Contato(self):
        pass

    def CadastrarUsuario(self):
        nome = self.tela_cadastro_usuario.lineEdit_5.text()
        cpf = self.tela_cadastro_usuario.lineEdit_7.text()
        telefone = self.tela_cadastro_usuario.lineEdit_8.text()
        email = self.tela_cadastro_usuario.lineEdit_9.text()
        if(self.tela_cadastro_usuario.radioButton.isChecked()):
            sexo = 'Masculino'
        else:
            sexo = 'Feminino'
        user = self.tela_cadastro_usuario.lineEdit_11.text()
        if(self.tela_cadastro_usuario.lineEdit_10.text() == self.tela_cadastro_usuario.lineEdit_12.text()):
            senha = self.tela_cadastro_usuario.lineEdit_10.text()
            dicio = {}
            dicio['nome'] = nome
            dicio['cpf'] = cpf
            dicio['telefone'] = telefone
            dicio['email'] = email
            dicio['sexo'] = sexo
            dicio['user'] = user
            dicio['senha'] = senha
            global Users
            usuario = User()
            usuario.Register(nome,cpf,telefone,email)
            usuario.RegUser(user,senha)
            self.AbrirTelaInicial()
            
            ########### socket comentado #############

            # self.conexao.sendMessage(str(dicio)) 
            # QtWidgets.QMessageBox.about(None, 'Importante', self.conexao.receiveMessage())
        # else:
            # QtWidgets.QMessageBox.about(None, 'Erro', 'As senhas não coincidem')
        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())