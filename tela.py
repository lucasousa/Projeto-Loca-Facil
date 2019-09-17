# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Cadastro.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from cadastro import Cliente, Cadastro



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(482, 280)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setWindowTitle("MainWindow")
        MainWindow.setAccessibleName("")
        MainWindow.setAccessibleDescription("")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 461, 241))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(70, 10, 381, 147))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_2.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_2.addWidget(self.lineEdit_5)
        self.widget1 = QtWidgets.QWidget(self.tab)
        self.widget1.setGeometry(QtCore.QRect(0, 10, 60, 151))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget1)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.widget1)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 170, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 60, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(70, 10, 381, 162))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_4.addWidget(self.lineEdit_6)
        self.line_2 = QtWidgets.QFrame(self.layoutWidget_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_4.addWidget(self.lineEdit_7)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_4.addWidget(self.lineEdit_8)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_4.addWidget(self.lineEdit_9)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_4.addWidget(self.lineEdit_10)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 180, 113, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(240, 180, 113, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser.setGeometry(QtCore.QRect(0, 10, 451, 171))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.tab_3)
        self.pushButton.setGeometry(QtCore.QRect(180, 180, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.cd = Cadastro()
        self.funcionalidades()

    def funcionalidades(self):
        self.pushButton_2.clicked.connect(self.cadastrar)
        self.pushButton_3.clicked.connect(self.buscar)
        self.pushButton_4.clicked.connect(self.alterar)
        self.pushButton.clicked.connect(self.listar)
        
    def listar(self):
        pass
        
    
    def alterar(self):
        global Clientes
        cpf_busca = self.lineEdit_6.text()
        encontrado = False
        for x in Clientes:
            if(x.cpf == cpf_busca):
                encontrado = True
                x.nome = self.lineEdit_7.text()
                x.endereco = self.lineEdit_8.text()
                x.cep = self.lineEdit_9.text()
                x.telefone = self.lineEdit_10.text()
                QtWidgets.QMessageBox.about(None, "Alteração", "Alterações realizadas com sucesso!",)
        if not encontrado:
            QtWidgets.QMessageBox.about(None, "Alteração", "CPF não encontrado!",)
            
    
    def buscar(self):
        global Clientes
        cpf_busca = self.lineEdit_6.text()
        encontrado = False
        for x in Clientes:
            if(x.cpf == cpf_busca):
                encontrado = True
                self.lineEdit_7.setText(x.nome)
                self.lineEdit_8.setText(x.endereco)
                self.lineEdit_9.setText(x.cep)
                self.lineEdit_10.setText(x.telefone)
        if(not encontrado):
            QtWidgets.QMessageBox.about(None, "Busca", "Valor de CPF não encontrado",)




    def cadastrar(self):
        nome  = self.lineEdit.text()
        cpf = self.lineEdit_2.text()
        endereco = self.lineEdit_3.text()
        CEP =  self.lineEdit_4.text()
        Telefone = self.lineEdit_5.text()
        global Clientes
        cl = Cliente(nome, cpf, endereco, CEP , Telefone)
        Clientes.append(cl)
        if(self.cd.verifica_cadastro(cl.cpf)):
            self.cd.cadastra(cl)
            QtWidgets.QMessageBox.about(None, "Cadastro", "Cliente cadastrado com sucesso!",)
        else:
            QtWidgets.QMessageBox.about(None, "Cadastro", "Esse CPF já existe em nosso sistema!")
        print(self.cd.getTotal())

    def mostraTodos(self):
        print(self.cl)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "Nome"))
        self.label_2.setText(_translate("MainWindow", "CPF"))
        self.label_3.setText(_translate("MainWindow", "Endereço"))
        self.label_4.setText(_translate("MainWindow", "CEP"))
        self.label_5.setText(_translate("MainWindow", "Telefone"))
        self.pushButton_2.setText(_translate("MainWindow", "Cadastrar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Cadastro"))
        self.label_7.setText(_translate("MainWindow", "CPF"))
        self.label_6.setText(_translate("MainWindow", "Nome"))
        self.label_8.setText(_translate("MainWindow", "Endereço"))
        self.label_9.setText(_translate("MainWindow", "CEP"))
        self.label_10.setText(_translate("MainWindow", "Telefone"))
        self.pushButton_3.setText(_translate("MainWindow", "Buscar"))
        self.pushButton_4.setText(_translate("MainWindow", "Alterar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Buscar e Alterar"))
        self.pushButton.setText(_translate("MainWindow", "Mostrar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Mostrar Todos"))

Clientes = []
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())