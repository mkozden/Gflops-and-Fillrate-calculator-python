"""
TODO:
find a way to get dynamic colors in table
dynamically change which gpu to compare against (on click maybe?)
"""
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
		self.gpus = []
		self.ui.AddGPU.clicked.connect(self.add_gpu)
		self.ui.RemoveGPU.clicked.connect(self.remove_gpu)
		self.ui.MainTable.cellPressed.connect(self.update_gpus)
		self.ui.chooseMemType.addItems(["GDDR3", "GDDR5", "GDDR5X", "GDDR6", "GDDR6X", "HBM", "HBM2"])
		self.ui.MainTable.setHorizontalHeaderLabels(["Specs", "GFLOPS", "Pixel Fillrate (GPixel/s)", "Texture Fillrate (GTexel/s)", "Bandwidth (GB/s)", "Average Difference (%)"])
		self.ui.MainTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
		self.ui.MainTable.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
		self.ui.MainTable.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
		for item in self.ui.verticalWidget.findChildren(QtWidgets.QLineEdit):
			item.setValidator(QIntValidator())
			item.textChanged.connect(self.reset_color)

	def compare_gpus(self, compared, reference, value):
		"""

		:param compared: GPU to be compared
		:param reference: GPU to be compared against (baseline)
		:param value: The value to be compared
		:return: Rich text containing a percentage value within QWidget Object
		"""
		if compared is not None:
			if reference is not None:
				if value == "avg":
					diff = 0
					methods = [func for func in dir(GPU) if callable(getattr(GPU, func)) and not func.startswith("__")]
					for method in methods:
						diff += ((getattr(compared, method)() - getattr(reference, method)())/getattr(reference, method)())*100
					diff = diff/len(methods)
				else:
					diff = ((getattr(compared, value)() - getattr(reference, value)())/getattr(reference, value)())*100
				if diff < 0:
					color = "red"
				elif diff > 0:
					color = "green"
				else:
					color = "black"
				widget = QtWidgets.QWidget()
				text = QtWidgets.QLabel(f"<br></br><br></br><font color={color}>{round(diff,3)}%</font>")
				widget_layout = QtWidgets.QHBoxLayout()
				widget_layout.addWidget(text)
				widget_layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
				widget.setLayout(widget_layout)
				return widget
			return 0
		return 0

	def add_gpu(self):
		if self.check_inputs() == 0:
			gpu = GPU(":".join([i.text() for i in self.ui.Core.findChildren(QtWidgets.QLineEdit)]),
			          self.ui.inputCoreHz.text(), self.ui.chooseMemType.currentText().lower(), self.ui.inputBusWidth.text(),
			          self.ui.inputMemHz.text())
			self.gpus.append(gpu)
			self.ui.MainTable.setRowCount(self.ui.MainTable.rowCount()+1)
			self.ui.MainTable.setItem(self.ui.MainTable.rowCount()-1, 0, QtWidgets.QTableWidgetItem(f"{gpu.core_cfg}\n{gpu.core_clk} MHz Core\n{gpu.mem_clk} MHz Memory\n{gpu.mem_type.upper()}"))
			self.ui.MainTable.setItem(self.ui.MainTable.rowCount()-1, 1, QtWidgets.QTableWidgetItem(str(gpu.gflops())))
			self.ui.MainTable.setItem(self.ui.MainTable.rowCount()-1, 2, QtWidgets.QTableWidgetItem(str(gpu.gpixels())))
			self.ui.MainTable.setItem(self.ui.MainTable.rowCount()-1, 3, QtWidgets.QTableWidgetItem(str(gpu.gtexels())))
			self.ui.MainTable.setItem(self.ui.MainTable.rowCount()-1, 4, QtWidgets.QTableWidgetItem(str(gpu.gbytes())))
			for item in self.ui.verticalWidget.findChildren(QtWidgets.QLineEdit):
				item.setText("")

	def update_gpus(self):
		reference_row = self.ui.MainTable.currentRow()
		for row in range(self.ui.MainTable.rowCount()):
			self.ui.MainTable.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{self.gpus[row].core_cfg}\n{self.gpus[row].core_clk} MHz Core\n{self.gpus[row].mem_clk} MHz Memory\n{self.gpus[row].mem_type.upper()}"))
			self.ui.MainTable.setCellWidget(row, 1, self.compare_gpus(self.gpus[row], self.gpus[reference_row], "gflops"))
			self.ui.MainTable.setCellWidget(row, 2, self.compare_gpus(self.gpus[row], self.gpus[reference_row], "gpixels"))
			self.ui.MainTable.setCellWidget(row, 3, self.compare_gpus(self.gpus[row], self.gpus[reference_row], "gtexels"))
			self.ui.MainTable.setCellWidget(row, 4, self.compare_gpus(self.gpus[row], self.gpus[reference_row], "gbytes"))
			self.ui.MainTable.setCellWidget(row, 5, self.compare_gpus(self.gpus[row], self.gpus[reference_row], "avg"))

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
		row = self.ui.MainTable.currentRow()
		print(row)
		self.ui.MainTable.removeRow(row)
		del self.gpus[row]



def window():
	app = QtWidgets.QApplication(sys.argv)
	win = Window()
	win.show()
	sys.exit(app.exec_())


window()
