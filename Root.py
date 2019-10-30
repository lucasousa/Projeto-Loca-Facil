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
from codigos_telas.pesquisar import Ui_Pesquisar
from PyQt5.QtGui import QPixmap
import PyQt5
import sys
import os
from PyQt5.QtCore import pyqtSlot
from classes import Person, Rent, Renter, User
from Comunicacao import Conex
import threading
from ast import literal_eval
import time

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
        self.stack9 = QtWidgets.QMainWindow()

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

        self.tela_pesquisar = Ui_Pesquisar()
        self.tela_pesquisar.setupUi(self.stack9)

        self.QtStack.addWidget(self.stack0) #Tela inicial
        self.QtStack.addWidget(self.stack1) #Tela login
        self.QtStack.addWidget(self.stack2) #Tela principal
        self.QtStack.addWidget(self.stack3) #Tela Cadastro de Usuário
        self.QtStack.addWidget(self.stack4) #Tela Cadastro de Imóvel
        self.QtStack.addWidget(self.stack5) #Tela de contato
        self.QtStack.addWidget(self.stack6) #Tela de recuperar login
        self.QtStack.addWidget(self.stack7) #Tela de sobre
        self.QtStack.addWidget(self.stack8) #Tela de cadastro de fotos do imóvel
        self.QtStack.addWidget(self.stack9) #Tela de pesquisar


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
        self.tela_login.pushButton.clicked.connect(self.login) #Botão Entrar

        #Main tela
        self.tela_principal.toolButton.clicked.connect(self.AbrirTelaCadImovel) #Cadastrar Imóvel
        self.tela_principal.toolButton_3.clicked.connect(self.Erro)             #Visualizar Imóveis
        self.tela_principal.toolButton_4.clicked.connect(self.AbrirTelaContato) #Contato
        self.tela_principal.toolButton_5.clicked.connect(self.AbrirTelaSobre)   #Sobre
        self.tela_principal.toolButton_2.clicked.connect(self.AbrirTelaInicial) #Encerrar Sessão
        self.tela_principal.toolButton_6.clicked.connect(self.AbrirTelaPesquisar)             #Buscar

        self.tela_contato.toolButton.clicked.connect(self.AbrirTelaPrincipal)           #Botão voltar (tela principal)
        self.tela_cadastro_imovel.toolButton.clicked.connect(self.AbrirTelaPrincipal)   #Botão voltar (tela principal)
        self.tela_cadastro_imovel.pushButton_2.clicked.connect(self.AbrirTelaPrincipal) #Botão cancelar cadastro de imóvel
        
        self.tela_login.toolButton_2.clicked.connect(self.AbrirTelaInicial)         #Voltar de login para tela inicial
        self.tela_login.toolButton.clicked.connect(self.AbrirTelaRecuperarLogin)    #Link para recuperar Login
        self.tela_recuperar_login.pushButton_2.clicked.connect(self.AbrirTelaLogin) #Voltar da tela de recuperar login para a  tela  de login
        

        #cadastro Usuário
        self.tela_cadastro_usuario.pushButton.clicked.connect(self.CadastrarUsuario)   #Cadastrar
        self.tela_cadastro_usuario.pushButton_2.clicked.connect(self.AbrirTelaInicial) #Cancelar
        
        #Cadastro Imóvel
        self.tela_cadastro_imovel.pushButton.clicked.connect(self.CadastrarImovel) #Abrindo tela de  cadastrar fotos e continuando o cadastro do imóvel

        #Sobre
        self.tela_sobre.toolButton.clicked.connect(self.AbrirTelaPrincipal)

        #contato
        self.tela_contato.pushButton.clicked.connect(self.Contato)


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
    def AbrirTelaPesquisar(self):
        self.QtStack.setCurrentIndex(9)

    def login(self):
        dic = {}
        dic['op'] = 'Login'
        dic['login'] = self.tela_login.lineEdit_7.text()
        dic['senha'] = self.tela_login.lineEdit_8.text()
        self.conexao.startConnection()
        self.conexao.sendMessage(str(dic))
        print("123")
        resp = self.conexao.receiveMessage()
        print("123")
        resp = literal_eval(resp)
        self.conexao.closeConnection()
        if(resp['status'] == 'success'): #busca no banco
            self.AbrirTelaPrincipal()
        else:
            QtWidgets.QMessageBox.about(None, 'Erro', 'usuário e/ou senha inválido(s)')


    def CadastrarImovel(self):
        dicio = {}
        dicio['op'] = 'CadImovel'
        dicio['desc'] = self.tela_cadastro_imovel.lineEdit_10.text()
        dicio['bairro'] = self.tela_cadastro_imovel.lineEdit_5.text()
        dicio['sit'] = 1
        dicio['rua'] = self.tela_cadastro_imovel.lineEdit_7.text()
        dicio['numero'] = self.tela_cadastro_imovel.lineEdit_9.text()
        dicio['complemento'] = self.tela_cadastro_imovel.lineEdit_8.text()
        dicio['cep'] = self.tela_cadastro_imovel.lineEdit_6.text()
        dicio['preco'] = self.tela_cadastro_imovel.lineEdit_11.text()
        dicio['id_user'] = self.tela_cadastro_imovel.lineEdit_12.text()
        
        verification = dicio['bairro'] == '' or dicio['rua'] == '' or dicio['numero'] == '' or len(dicio['cep']) != 8 or len(dicio['id_user']) != 11
        if(verification):
            QtWidgets.QMessageBox.about(None, 'Erro', 'Preencha todos os campos de forma correta')
        else:
            self.conexao.startConnection()
            self.conexao.sendMessage(str(dicio))

            resp = literal_eval(self.conexao.receiveMessage())
            if(resp['status']=='success'):
                QtWidgets.QMessageBox.about(None, 'Importante', 'Cadastro realizado com sucesso')
                self.AbrirTelaCadastroFotos()
            else:
                QtWidgets.QMessageBox.about(None, 'Importante', 'Ocorreu um erro de conexão, tente novamente mais tarde')
            self.conexao.closeConnection()
            

    def Contato(self):
        dic={}
        dic['op'] = 'Contato' 
        dic['nome'] = self.tela_contato.lineEdit_7.text()
        dic['email'] = self.tela_contato.lineEdit_8.text()
        dic['message'] = self.tela_contato.lineEdit_9.text()
        self.conexao.startConnection()
        self.conexao.sendMessage(str(dic))
        resp = literal_eval(self.conexao.receiveMessage())
        if(resp['status'] == 'success'):
            QtWidgets.QMessageBox.about(None, 'Importante', 'Sua Mensagem foi enviada com sucesso')
        else:
            QtWidgets.QMessageBox.about(None, 'Importante', 'Não conseguimos contato, por favor tente mais tarde')
        self.conexao.closeConnection()
        self.AbrirTelaPrincipal()

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
        verification = nome == '' or cpf == '' or telefone == '' or email == '' or not '@' in email 
        print(verification)
        if(self.tela_cadastro_usuario.lineEdit_10.text() != self.tela_cadastro_usuario.lineEdit_12.text()):
            QtWidgets.QMessageBox.about(None, 'Erro', 'As senhas não coincidem')
        elif len(cpf) != 11 :
            QtWidgets.QMessageBox.about(None, 'Erro', 'cpf inválido')
        elif(not verification):
            dic = {}
            dic['op'] = 'VerifyCadUser'
            dic['usuario'] = user
            self.conexao.startConnection()
            self.conexao.sendMessage(str(dic))
            resp = literal_eval(self.conexao.receiveMessage())
            self.conexao.closeConnection()
            if(resp['status'] == 'success'):

                senha = self.tela_cadastro_usuario.lineEdit_10.text()
                dicio = {}
                dicio['op'] = 'CadUser'
                dicio['nome'] = nome
                dicio['cpf'] = cpf
                dicio['telefone'] = telefone
                dicio['email'] = email
                dicio['sexo'] = sexo
                dicio['usuario'] = user
                dicio['senha'] = senha
                self.conexao.startConnection()
                self.conexao.sendMessage(str(dicio))
                self.conexao.receiveMessage()
                self.conexao.closeConnection()
                self.AbrirTelaInicial()
            else:
                QtWidgets.QMessageBox.about(None, 'Erro', 'Esse usuário já existe')
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())