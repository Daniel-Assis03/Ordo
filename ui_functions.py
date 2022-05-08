from main import *

class UIFunctions(MainWindow):

    def uiDefinitions(self):
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.btn_min.clicked.connect(lambda: self.showMinimized())

        self.btn_close.clicked.connect(lambda: self.close())

        self.frame.setStyleSheet("border-radius:15px;")