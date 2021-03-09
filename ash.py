#PRIMARY IMPORTS

import PySide2, PyQt5, sys, os, platform

#SECONDARY IMPORTS

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QIcon)
from PySide2.QtWidgets import *
from PyQt5 import *

#UI IMPORTS

from data.ui_splash_screen import Ui_SplashScreen

#SETTINGS

counter = 0

#MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet("""color: rgba(255,255,255,100%); background-color: rgba(34,34,34,100%); border-radius: 150px;""")
        self.setFixedSize(750, 600)
        self.setWindowIcon(QtGui.QIcon("./data/imgs/icon.png"))
        self.setWindowTitle("Ash - Edit")
        
        self.editor = QPlainTextEdit() 
        self.setCentralWidget(self.editor)
        fixedfont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        fixedfont.setPointSize(12)
        self.editor.setFont('ArialFont')

        self.path = None



# SPLASH SCREEN
class SplashScreen(QMainWindow):
    is_save = False
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("./data/imgs/icon.png"))
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(60)

        self.ui.label_description.setText("<strong>Welcome to ash</strong>")

        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>Loading Database</strong>"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>Loading User Interface</strong>"))
		
        self.show()

    #COUNTER
    def progress(self):
        global counter
        self.ui.progressBar.setValue(counter)
        if counter > 100:
            self.timer.stop()
            self.main = MainWindow()
            self.main.show()
            self.close()
        counter += 1    

#LAUNCH APPLICATION
def launch():

		# First we created a application object for pyqt

		app = QApplication(sys.argv)

		# Next is we show the window then execute the app.

		window = SplashScreen()
		window.show()
		sys.exit(app.exec_())

if __name__ == '__main__':

	launch()