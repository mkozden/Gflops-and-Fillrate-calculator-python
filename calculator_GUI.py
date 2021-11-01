from PyQt5 import QtWidgets
from PyQt5.QtGui import QIntValidator
import sys
from calcui import Ui_MainWindow
from calculator_CLI import GPU


class Window(QtWidgets.QMainWindow):
	def __init__(self):
		super(Window, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.AddGPU.clicked.connect(self.add_gpu)
		self.ui.RemoveGPU.clicked.connect(self.remove_gpu)
		self.ui.chooseMemType.addItems(["GDDR3", "GDDR5", "GDDR5X", "GDDR6", "GDDR6X", "HBM", "HBM2"])
		self.ui.MainTable.setHorizontalHeaderLabels(["Core Config", "GFLOPS", "Pixel Fillrate (GPixel/s)", "Texture Fillrate (GTexel/s)", "Bandwidth (GB/s)", "Average Difference (%)"])
		self.ui.MainTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
		for item in self.ui.verticalWidget.findChildren(QtWidgets.QLineEdit):
			item.setValidator(QIntValidator())
			item.textChanged.connect(self.reset_color)

	def add_gpu(self):
		if self.check_inputs() == 0:
			gpu = GPU(":".join([i.text() for i in self.ui.Core.findChildren(QtWidgets.QLineEdit)]),
			          self.ui.inputCoreHz.text(), self.ui.chooseMemType.currentText().lower(), self.ui.inputBusWidth.text(),
			          self.ui.inputMemHz.text())
			self.ui.MainTable.setRowCount(self.ui.MainTable.rowCount()+1)
			self.ui.MainTable.setItem(self.ui.MainTable.rowCount()-1, 0, QtWidgets.QTableWidgetItem(gpu.core_cfg))
			self.ui.MainTable.setItem(self.ui.MainTable.rowCount()-1, 1, QtWidgets.QTableWidgetItem(str(gpu.gflops())))
			self.ui.MainTable.setItem(self.ui.MainTable.rowCount()-1, 2, QtWidgets.QTableWidgetItem(str(gpu.gpixels())))
			self.ui.MainTable.setItem(self.ui.MainTable.rowCount()-1, 3, QtWidgets.QTableWidgetItem(str(gpu.gtexels())))
			self.ui.MainTable.setItem(self.ui.MainTable.rowCount()-1, 4, QtWidgets.QTableWidgetItem(str(gpu.gbytes())))
			for item in self.ui.verticalWidget.findChildren(QtWidgets.QLineEdit):
				item.setText("")

	def check_inputs(self):
		has_error = 0
		for item in self.ui.verticalWidget.findChildren(QtWidgets.QLineEdit):
			if item.text() == "":
				item.setStyleSheet("QLineEdit { background-color: rgb(255,192,192);}")
				has_error = 1
		return has_error

	def reset_color(self):
		item = self.sender()
		item.setStyleSheet("QLineEdit { background-color: rgb(255,255,255);}")

	def remove_gpu(self):
		self.ui.MainTable.removeRow(self.ui.MainTable.currentRow())



def window():
	app = QtWidgets.QApplication(sys.argv)
	win = Window()
	win.show()
	sys.exit(app.exec_())


window()
