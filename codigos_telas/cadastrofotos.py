# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fotos_ap.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon

class Ui_cadastrofotos(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 18, 201, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(95, 90, 260, 41))
        self.textBrowser_2.setStyleSheet("border: none;\n"
"")
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(103, 135, 171, 41))
        self.label_3.setStyleSheet("background-color: #6D676E;\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(177, 140, 91, 31))
        self.toolButton_2.setStyleSheet("background-color: #345995;\n"
"font: 75 9pt \"Gadugi\";\n"
"color: #FFFFFF;\n"
"")
        self.toolButton_2.setObjectName("toolButton_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(304, 135, 171, 41))
        self.label_4.setStyleSheet("background-color: #6D676E;\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.toolButton_3 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_3.setGeometry(QtCore.QRect(378, 141, 91, 31))
        self.toolButton_3.setStyleSheet("background-color: #345995;\n"
"font: 75 9pt \"Gadugi\";\n"
"color: #FFFFFF;\n"
"")
        self.toolButton_3.setObjectName("toolButton_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(506, 135, 171, 41))
        self.label_6.setStyleSheet("background-color: #6D676E;\n"
"color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.toolButton_5 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_5.setGeometry(QtCore.QRect(580, 141, 91, 31))
        self.toolButton_5.setStyleSheet("background-color: #345995;\n"
"font: 75 9pt \"Gadugi\";\n"
"color: #FFFFFF;\n"
"")
        self.toolButton_5.setObjectName("toolButton_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 250, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("color: #FFFFFF;\n"
"background-color: #0A8754;")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def pushButton_handler(self):
        print("Botão pressionado")
        return self.open_dialog_box()

    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        return path

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Imagens | Imóvel"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600; color:#ff0000;\">*</span><span style=\" font-weight:600;\"> Adicione algumas fotos do imóvel</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "   Imagem 1"))
        self.toolButton_2.setText(_translate("MainWindow", "Procurar"))
        self.label_4.setText(_translate("MainWindow", "   Imagem 2"))
        self.toolButton_3.setText(_translate("MainWindow", "Procurar"))
        self.label_6.setText(_translate("MainWindow", "   Imagem 3"))
        self.toolButton_5.setText(_translate("MainWindow", "Procurar"))
        self.pushButton.setText(_translate("MainWindow", "Confirmar"))
        self.toolButton_2.clicked.connect(self.pushButton_handler)
        self.toolButton_3.clicked.connect(self.pushButton_handler)
        self.toolButton_5.clicked.connect(self.pushButton_handler)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_cadastrofotos()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

