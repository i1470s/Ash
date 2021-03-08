#PRIMARY IMPORTS

import PyQt5

#SECONDARY IMPORTS

from PyQt5.QtWidgets import ( QMainWindow, QLabel, QDesktopWidget, QHBoxLayout,QFileDialog )
from PyQt5.QtCore import Qt, QSettings, QSize, QPoint

class App(QMainWindow):
	is_save = False

	def __init__(self):
		super(App, self).__init__()
		self.setWindowTitle("Ash")
		
		self.setGeometry(0, 0, 700, 600)
		#self.setWindowFlag(Qt.FramelessWindowHint)
		resolution = QDesktopWidget().screenGeometry()
		self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
			(resolution.height() / 2) - (self.frameSize().height() / 2))
