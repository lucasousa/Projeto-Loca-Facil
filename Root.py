from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QTableWidgetItem
from Telas.telainicial import Ui_telainicial
from Telas.login import Ui_login
from Telas.maintela import Ui_maintela
from Telas.cadastroimovel import Ui_cadastroimovel
from Telas.cadastrousuario import Ui_cadastrousuario
from PyQt5.QtGui import QPixmap
import PyQt5
import sys
import os
from PyQt5.QtCore import pyqtSlot

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

        self.QtStack.addWidget(self.stack0) #Tela inicial
        self.QtStack.addWidget(self.stack1) #Tela login
        self.QtStack.addWidget(self.stack2) #Tela principal
        self.QtStack.addWidget(self.stack3) #Tela Cadastro de Usuário
        self.QtStack.addWidget(self.stack4) #Tela Cadastro de Imóvel


class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        #Tela inicial
        self.tela_inicio.pushButton.clicked.connect(self.stack3) #Botão cadastrar
        self.tela_inicio.pushButton_2.clicked.connect(self.stack1) #Botão Login
        #login
        self.tela_login.pushButton.clicked.connect(self.stack2) #Botão Entrar 
        #Main tela
        self.tela_principal.toolButton.clicked.connect(self.stack4) #Cadastrar Imóvel
        self.tela_principal.toolButton_2.clicked.connect(NotImplemented) #Visualizar Imóveis
        self.tela_principal.toolButton_3.clicked.connect(NotImplemented) #Sobre
        self.tela_principal.toolButton_4.clicked.connect(NotImplemented) #Contato
        #cadastro Usuário
        self.tela_cadastro_usuario.pushButton.clicked.connect(self.stack2) #Cadastrar
        #Cadastro Imóvel
        self.tela_cadastro_imovel.pushButton.clicked.connect(self.stack2) #Cadastrar
        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())