# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fotos_ap.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
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
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(90, 78, 540, 41))
        self.textBrowser.setStyleSheet("border: none;\n"
"")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(97, 126, 211, 41))
        self.label_2.setStyleSheet("background-color: #6D676E;\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(210, 133, 91, 31))
        self.toolButton.setStyleSheet("background-color: #345995;\n"
"font: 75 9pt \"Gadugi\";\n"
"color: #FFFFFF;\n"
"")
        self.toolButton.setObjectName("toolButton")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(90, 190, 540, 41))
        self.textBrowser_2.setStyleSheet("border: none;\n"
"")
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 222, 211, 41))
        self.label_3.setStyleSheet("background-color: #6D676E;\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(213, 227, 91, 31))
        self.toolButton_2.setStyleSheet("background-color: #345995;\n"
"font: 75 9pt \"Gadugi\";\n"
"color: #FFFFFF;\n"
"")
        self.toolButton_2.setObjectName("toolButton_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 272, 211, 41))
        self.label_4.setStyleSheet("background-color: #6D676E;\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.toolButton_3 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_3.setGeometry(QtCore.QRect(213, 279, 91, 31))
        self.toolButton_3.setStyleSheet("background-color: #345995;\n"
"font: 75 9pt \"Gadugi\";\n"
"color: #FFFFFF;\n"
"")
        self.toolButton_3.setObjectName("toolButton_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(99, 323, 211, 41))
        self.label_5.setStyleSheet("background-color: #6D676E;\n"
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.toolButton_4 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_4.setGeometry(QtCore.QRect(212, 330, 91, 31))
        self.toolButton_4.setStyleSheet("background-color: #345995;\n"
"font: 75 9pt \"Gadugi\";\n"
"color: #FFFFFF;\n"
"")
        self.toolButton_4.setObjectName("toolButton_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(99, 373, 211, 41))
        self.label_6.setStyleSheet("background-color: #6D676E;\n"
"color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.toolButton_5 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_5.setGeometry(QtCore.QRect(212, 380, 91, 31))
        self.toolButton_5.setStyleSheet("background-color: #345995;\n"
"font: 75 9pt \"Gadugi\";\n"
"color: #FFFFFF;\n"
"")
        self.toolButton_5.setObjectName("toolButton_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(99, 423, 211, 41))
        self.label_7.setStyleSheet("background-color: #6D676E;\n"
"color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.toolButton_6 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_6.setGeometry(QtCore.QRect(211, 430, 91, 31))
        self.toolButton_6.setStyleSheet("background-color: #345995;\n"
"font: 75 9pt \"Gadugi\";\n"
"color: #FFFFFF;\n"
"")
        self.toolButton_6.setObjectName("toolButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def pushButton_handler(self):
        print("Botão pressionado")
        self.open_dialog_box()
    
    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        print(path)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Cadastro | Imóvel"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600; color:#ff0000;\">*</span><span style=\" font-weight:600;\"> Anexe algum documento que comprove que você é proprietário do imóvel (ex: contrato, conta de energia, conta de água...)</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "  Adicionar arquivo"))
        self.toolButton.setText(_translate("MainWindow", "Procurar"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600; color:#ff0000;\">*</span><span style=\" font-weight:600;\"> Adicione algumas fotos do imóvel</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "  Adicionar arquivo"))
        self.toolButton_2.setText(_translate("MainWindow", "Procurar"))
        self.label_4.setText(_translate("MainWindow", "  Adicionar arquivo"))
        self.toolButton_3.setText(_translate("MainWindow", "Procurar"))
        self.label_5.setText(_translate("MainWindow", "  Adicionar arquivo"))
        self.toolButton_4.setText(_translate("MainWindow", "Procurar"))
        self.label_6.setText(_translate("MainWindow", "  Adicionar arquivo"))
        self.toolButton_5.setText(_translate("MainWindow", "Procurar"))
        self.label_7.setText(_translate("MainWindow", "  Adicionar arquivo"))
        self.toolButton_6.setText(_translate("MainWindow", "Procurar"))
        self.toolButton.clicked.connect(self.pushButton_handler)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
