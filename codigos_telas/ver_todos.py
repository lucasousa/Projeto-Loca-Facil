# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ver_todos.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ver_todos(object):
    def loadData(self, lista):
        self.tableWidget.setVerticalHeaderLabels(["Bairro","Preço","Rua","Ver Mais"])
        self.tableWidget.setRowCount(0)
        for row_number in range(len(lista)):
            self.tableWidget.insertRow(row_number)
            self.tableWidget.setItem(row_number, 0, QtWidgets.QTableWidgetItem(lista[row_number]['bairro']))
            self.tableWidget.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str(lista[row_number]['preco'])))
            self.tableWidget.setItem(row_number, 2, QtWidgets.QTableWidgetItem(lista[row_number]['rua']))
            btn = QtWidgets.QPushButton(self.tableWidget)
            btn.setText("ver Informações")
            btn.setStyleSheet("background-color: #345995;\n"
"color: #FFFFFF;")
            self.tableWidget.setCellWidget(row_number, 3, btn)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(880, 600)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(29, 100, 820, 431))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(40, 30, 60, 41))
        self.toolButton.setStyleSheet("border: none;\n"
"")
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagens/back_12955.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(32, 32))
        self.toolButton.setObjectName("toolButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
