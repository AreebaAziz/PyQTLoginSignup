import sys

from PyQt5.QtWidgets import QApplication

from .views.mainwindow import MainWindow

def run():
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	app.exec_()