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
        self.toolButton.setGeometry(QtCore.QRect(20, 30, 150, 41))
        self.toolButton.setMinimumSize(QtCore.QSize(150, 40))
        self.toolButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Gadugi\";\n"
"background-color: rgb(8, 61, 119);\n"
"border-radius: 10px;\n"
"")
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(328, 30, 150, 41))
        self.toolButton_2.setMinimumSize(QtCore.QSize(150, 40))
        self.toolButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Gadugi\";\n"
"background-color: rgb(8, 61, 119);\n"
"border-radius: 10px;\n"
"")
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_3.setGeometry(QtCore.QRect(174, 30, 151, 41))
        self.toolButton_3.setMinimumSize(QtCore.QSize(150, 40))
        self.toolButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Gadugi\";\n"
"background-color: rgb(8, 61, 119);\n"
"border-radius: 10px;\n"
"")
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_4 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_4.setGeometry(QtCore.QRect(481, 30, 151, 41))
        self.toolButton_4.setMinimumSize(QtCore.QSize(150, 40))
        self.toolButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Gadugi\";\n"
"background-color: rgb(8, 61, 119);\n"
"border-radius: 10px;\n"
"")
        self.toolButton_4.setObjectName("toolButton_4")
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
        self.toolButton_2.setText(_translate("MainWindow", "Sobre"))
        self.toolButton_3.setText(_translate("MainWindow", "Visualizar Imóveis"))
        self.toolButton_4.setText(_translate("MainWindow", "Contato"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
