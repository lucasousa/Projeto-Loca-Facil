# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ver_todos.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ver_todos(object):
    def loadData(self, lista):
        self.tableWidget.setRowCount(0)
        self.buttons = []
        self.infos = []
        for row_number in range(len(lista)):
            self.tableWidget.insertRow(row_number)
            self.tableWidget.setItem(row_number, 0, QtWidgets.QTableWidgetItem(lista[row_number]['bairro']))
            self.tableWidget.setItem(row_number, 1, QtWidgets.QTableWidgetItem(lista[row_number]['rua']))
            self.tableWidget.setItem(row_number, 2, QtWidgets.QTableWidgetItem(str(lista[row_number]['preco'])))
            self.tableWidget.setItem(row_number, 3, QtWidgets.QTableWidgetItem(lista[row_number]['nome']))
            self.tableWidget.setItem(row_number, 4, QtWidgets.QTableWidgetItem(lista[row_number]['telefone']))
            self.infos.append(lista[row_number])
            self.buttons.append(QtWidgets.QPushButton(self.tableWidget))
            self.buttons[-1].setText("ver foto")
            self.buttons[-1].setStyleSheet("background-color: #345995;\n"
            "color: #FFFFFF;")
            self.tableWidget.setCellWidget(row_number, 5, self.buttons[-1])
        print(self.buttons)
        print(self.infos)
        print(len(self.buttons))
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1083, 724)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(40, 60, 60, 41))
        self.toolButton.setStyleSheet("border: none;\n"
"")
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagens/back_12955.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(28, 28))
        self.toolButton.setObjectName("toolButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(130, 130, 871, 461))
        self.tableWidget.setStyleSheet("background-color: #F2F4F3;\n"
"font: 75 10pt \"Arial\";\n"
"font-weight:bold;")
        self.tableWidget.setGridStyle(QtCore.Qt.DashDotDotLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Bairro"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Rua"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Preço"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Proprietário"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Telefone"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Foto"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
