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
        MainWindow.resize(1006, 611)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(53, 5, 150, 41))
        self.toolButton.setMinimumSize(QtCore.QSize(150, 40))
        self.toolButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 9pt \"Gadugi\";\n"
"background-color: #662C91;\n"
"\n"
"\n"
"")
        self.toolButton.setObjectName("toolButton")
        self.toolButton_3 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_3.setGeometry(QtCore.QRect(203, 5, 150, 41))
        self.toolButton_3.setMinimumSize(QtCore.QSize(150, 40))
        self.toolButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 9pt \"Gadugi\";\n"
"background-color: #662C91;\n"
"hover{\n"
"    color: pink;\n"
"}\n"
"\n"
"")
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_4 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_4.setGeometry(QtCore.QRect(353, 5, 150, 41))
        self.toolButton_4.setMinimumSize(QtCore.QSize(150, 40))
        self.toolButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 9pt \"Gadugi\";\n"
"background-color: #662C91;\n"
"hover{\n"
"    color: pink;\n"
"}\n"
"\n"
"")
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolButton_5 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_5.setGeometry(QtCore.QRect(503, 5, 150, 41))
        self.toolButton_5.setMinimumSize(QtCore.QSize(150, 40))
        self.toolButton_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 9pt \"Gadugi\";\n"
"background-color: #662C91;\n"
"hover{\n"
"    color: pink;\n"
"}\n"
"\n"
"")
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolButton_6 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_6.setGeometry(QtCore.QRect(653, 5, 150, 41))
        self.toolButton_6.setMinimumSize(QtCore.QSize(150, 40))
        self.toolButton_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 9pt \"Gadugi\";\n"
"background-color: #662C91;\n"
"hover{\n"
"    color: pink;\n"
"}\n"
"\n"
"")
        self.toolButton_6.setObjectName("toolButton_6")
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(840, 0, 101, 51))
        self.toolButton_2.setStyleSheet("border: none;")
        self.toolButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagens/sair.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon)
        self.toolButton_2.setIconSize(QtCore.QSize(36, 36))
        self.toolButton_2.setObjectName("toolButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(830, 60, 121, 31))
        self.textBrowser.setStyleSheet("border: none;")
        self.textBrowser.setObjectName("textBrowser")
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
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#A52A2A;\">Encerrar Sessão</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
