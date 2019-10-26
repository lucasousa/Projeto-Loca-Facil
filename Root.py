from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QTableWidgetItem
from codigos_telas.telainicial import Ui_telainicial
from codigos_telas.login import Ui_login
from codigos_telas.maintela import Ui_maintela
from codigos_telas.cadastroimovel import Ui_cadastroimovel
from codigos_telas.cadastrousuario import Ui_cadastrousuario
from codigos_telas.contato import Ui_contato
from codigos_telas.sobre import Ui_Sobre
from codigos_telas.recuperar_login import Ui_recuperar_login
from codigos_telas.cadastrofotos import Ui_cadastrofotos
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
        self.stack7 = QtWidgets.QMainWindow()
        self.stack8 = QtWidgets.QMainWindow()

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

        self.tela_sobre = Ui_Sobre()
        self.tela_sobre.setupUi(self.stack7)

        self.tela_cadastrofoto = Ui_cadastrofotos()
        self.tela_cadastrofoto.setupUi(self.stack8)

        self.QtStack.addWidget(self.stack0) #Tela inicial
        self.QtStack.addWidget(self.stack1) #Tela login
        self.QtStack.addWidget(self.stack2) #Tela principal
        self.QtStack.addWidget(self.stack3) #Tela Cadastro de Usuário
        self.QtStack.addWidget(self.stack4) #Tela Cadastro de Imóvel
        self.QtStack.addWidget(self.stack5) #Tela de contato
        self.QtStack.addWidget(self.stack6) #Tela de recuperar login
        self.QtStack.addWidget(self.stack7) #Tela de sobre
        self.QtStack.addWidget(self.stack8) #Tela de cadastro de fotos do imóvel


class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        try:
            self.conexao = Conex('localhost', 7000)
        except:
            QtWidgets.QMessageBox.about(None, 'Erro', 'Não foi possível conectar ao servidor, tente novamente mais tarde')
            exit(-1)

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
        self.tela_principal.toolButton_4.clicked.connect(self.AbrirTelaContato) #Contato
        self.tela_principal.toolButton_5.clicked.connect(self.AbrirTelaSobre) #Sobre
        self.tela_principal.toolButton_2.clicked.connect(self.AbrirTelaInicial) #Encerrar Sessão
        self.tela_principal.toolButton_6.clicked.connect(self.Erro) #Buscar

        self.tela_contato.toolButton.clicked.connect(self.AbrirTelaPrincipal)         #Botão voltar (tela principal)
        self.tela_cadastro_imovel.toolButton.clicked.connect(self.AbrirTelaPrincipal) #Botão voltar (tela principal)
        self.tela_cadastro_imovel.pushButton_2.clicked.connect(self.AbrirTelaPrincipal) #Botão cancelar cadastro de imóvel
        
        self.tela_login.toolButton_2.clicked.connect(self.AbrirTelaInicial) #Voltar de login para tela inicial
        self.tela_login.toolButton.clicked.connect(self.AbrirTelaRecuperarLogin) #Link para recuperar Login
        self.tela_recuperar_login.pushButton_2.clicked.connect(self.AbrirTelaLogin) #Voltar da tela de recuperar login para a  tela  de login

        #cadastro Usuário
        self.tela_cadastro_usuario.pushButton.clicked.connect(self.CadastrarUsuario) #Cadastrar
        self.tela_cadastro_usuario.pushButton_2.clicked.connect(self.AbrirTelaInicial) #Cancelar
        
        #Cadastro Imóvel
        self.tela_cadastro_imovel.pushButton.clicked.connect(self.AbrirTelaCadastroFotos) #Abrindo tela de  cadastrar fotos e continuando o cadastro do imóvel

        #Sobre
        self.tela_sobre.toolButton.clicked.connect(self.AbrirTelaPrincipal)
    
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
    def AbrirTelaSobre(self):
        self.QtStack.setCurrentIndex(7)
    def AbrirTelaCadastroFotos(self):
        self.QtStack.setCurrentIndex(8)


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
        if(len(dicio['cpf'])!=11):
            QtWidgets.QMessageBox.about(None, 'Erro', 'cpf inválido')
        else:
            self.conexao.startConnection()
            while(resp['status']!='success'):
                self.conexao.sendMessage(str(dicio))
                resp = self.conexao.receiveMessage()
            self.conexao.closeConnection()
        self.AbrirTelaPrincipal()
            

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
        if(self.tela_cadastro_usuario.lineEdit_10.text() != self.tela_cadastro_usuario.lineEdit_12.text()):
            QtWidgets.QMessageBox.about(None, 'Erro', 'As senhas não coincidem')
        elif len(cpf) != 11 :
            QtWidgets.QMessageBox.about(None, 'Erro', 'cpf inválido')
        else:
            senha = self.tela_cadastro_usuario.lineEdit_10.text()
            dicio = {}
            dicio['name'] = nome
            dicio['cpf'] = cpf
            dicio['telephone'] = telefone
            dicio['email'] = email
            dicio['sex'] = sexo
            dicio['user'] = user
            dicio['password'] = senha
            global Users
            usuario = User()
            usuario.Register(nome,cpf,telefone,email)
            usuario.RegUser(user,senha)
            self.conexao.startConnection()
            self.conexao.sendMessage(str(dicio))
            self.conexao.receiveMessage()
            self.conexao.closeConnection()
            self.AbrirTelaInicial()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())