from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys

Form, _ = uic.loadUiType("design3.ui")


class Ui(QtWidgets.QDialog, Form):
    def __init__(self):
        super(Ui, self).__init__()
        self.setupUi(self)
        self.products = SuitableProducts()

        self.pushButton.clicked.connect(self.search)

    def search(self):
        sku = self.lineEdit.text()
        month = self.comboBox_4.text()
        region = self.comboBox_3.text()
        city = self.comboBox_2.text()
        filial = self.comboBox.text()


    def view_products(self):
        self.products.setModel(self.products_model)

    def view_graph(self):
        ...

    def view_wd_nd(self):
        ...


class SuitableProducts(QtCore.QAbstractListModel):
    def __init__(self, data=[], parent=None):
        QtCore.QAbstractListModel.__init__(self, parent)
        self.__data = data

    def rowCount(self, parent):
        return len(self.__data)

    def data(self, index):
        row = index.row()
        value = self.__data[row]
        return value

    def setData(self, index, value):
        row = index.row()
        data_value = value
        self.__data[row][0] = data_value
        self.dataChanged.emit(index, index)


app = QtWidgets.QApplication([])
win = uic.loadUi("design4.ui")  # расположение вашего файла .ui

win.show()
sys.exit(app.exec())
