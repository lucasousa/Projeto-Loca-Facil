# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastro_usuário.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_cadastrousuario(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 90, 721, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(569, 224, 71, 40))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(170, 230, 41, 40))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(649, 300, 100, 20))
        self.radioButton.setObjectName("radioButton")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(250, 370, 531, 40))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(170, 290, 51, 40))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(576, 290, 46, 40))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(170, 543, 101, 40))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(170, 160, 59, 40))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(779, 300, 100, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(170, 420, 59, 40))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 620, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color: #345995;\n"
"color: #FFFFFF;")
        self.pushButton.setObjectName("pushButton")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(170, 480, 59, 40))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(280, 166, 621, 31))
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(277, 234, 271, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(650, 230, 250, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(278, 294, 271, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(280, 428, 271, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(280, 489, 271, 31))
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(281, 547, 271, 31))
        self.lineEdit_7.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(769, 625, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("color: #FFFFFF;\n"
"background-color: rgb(253, 27, 27);")
        self.pushButton_2.setIconSize(QtCore.QSize(15, 0))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Cadastro | Usuário"))
        self.label_7.setText(_translate("MainWindow", "Telefone"))
        self.label_6.setText(_translate("MainWindow", "CPF"))
        self.radioButton.setText(_translate("MainWindow", "Masculino"))
        self.label_13.setText(_translate("MainWindow", "* Agora crie um usuário e senha pra fazer login no LocaFácil"))
        self.label_8.setText(_translate("MainWindow", "E-mail"))
        self.label_9.setText(_translate("MainWindow", "Sexo"))
        self.label_12.setText(_translate("MainWindow", "Repetir Senha"))
        self.label_5.setText(_translate("MainWindow", "Nome"))
        self.radioButton_2.setText(_translate("MainWindow", "Feminino"))
        self.label_10.setText(_translate("MainWindow", "Usuário"))
        self.pushButton.setText(_translate("MainWindow", "Cadastrar"))
        self.label_11.setText(_translate("MainWindow", "Senha"))
        self.pushButton_2.setText(_translate("MainWindow", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
