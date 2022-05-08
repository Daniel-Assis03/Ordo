import os
import shutil
from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon
from ui_main import *
from ui_functions import *
import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Organizador de Arquivos")
        icon = QIcon("logo.ico")
        self.setWindowIcon(icon)

        UIFunctions.uiDefinitions(self)

        def moveWindow(event):
            
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()


        self.frame.mouseMoveEvent = moveWindow 

        self.file = ''

        self.btn_abrir.clicked.connect(self.abrir)
        self.btn_organizar.clicked.connect(self.organizar)

        

    def abrir(self):
        self.file = QFileDialog.getExistingDirectory(self, str("pasta"),'/home',
                                                QFileDialog.ShowDirsOnly |
                                                QFileDialog.DontResolveSymlinks)
        self.caminho.setText(self.file)
        self.file = str(self.file)


    def organizar(self):

        try:
            path = self.file
            files = os.listdir(path)
            for file in files:
                    filename, extension = os.path.splitext(file)
                    extension = extension[1:]
                    
                    if os.path.exists(path + '/' + extension):
                        shutil.move(path + '/' + file, path + '/' + extension + '/' + file)

                    else:
                        os.makedirs(path + '/' + extension)
                        shutil.move(path + '/' + file, path +'/' + extension)


            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Arquivos Organizados")
            msg.exec_() 
        except:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("É preciso selecionar uma pasta antes")
                msg.exec_() 

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()