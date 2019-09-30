# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_tela.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_maintela(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(943, 600)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(27, 0, 170, 41))
        self.toolButton.setMinimumSize(QtCore.QSize(150, 40))
        self.toolButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Gadugi\";\n"
"background-color: #662C91;\n"
"\n"
"")
        self.toolButton.setObjectName("toolButton")
        self.toolButton_3 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_3.setGeometry(QtCore.QRect(196, 0, 180, 41))
        self.toolButton_3.setMinimumSize(QtCore.QSize(150, 40))
        self.toolButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Gadugi\";\n"
"background-color: #662C91;\n"
"\n"
"")
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_4 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_4.setGeometry(QtCore.QRect(376, 0, 180, 41))
        self.toolButton_4.setMinimumSize(QtCore.QSize(150, 40))
        self.toolButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Gadugi\";\n"
"background-color: #662C91;\n"
"\n"
"")
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolButton_5 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_5.setGeometry(QtCore.QRect(556, 0, 180, 41))
        self.toolButton_5.setMinimumSize(QtCore.QSize(150, 40))
        self.toolButton_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Gadugi\";\n"
"background-color: #662C91;\n"
"\n"
"")
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolButton_6 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_6.setGeometry(QtCore.QRect(736, 0, 180, 41))
        self.toolButton_6.setMinimumSize(QtCore.QSize(150, 40))
        self.toolButton_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Gadugi\";\n"
"background-color: #662C91;\n"
"\n"
"")
        self.toolButton_6.setObjectName("toolButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolButton.setText(_translate("MainWindow", "Cadastrar Imóvel"))
        self.toolButton_3.setText(_translate("MainWindow", "Ver Imóveis"))
        self.toolButton_4.setText(_translate("MainWindow", "Contato"))
        self.toolButton_5.setText(_translate("MainWindow", "Sobre"))
        self.toolButton_6.setText(_translate("MainWindow", "Buscar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
