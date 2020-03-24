import sys
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "App"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        buttonWindow1 = QPushButton('Window1', self)
        buttonWindow1.move(100, 100)
        buttonWindow1.clicked.connect(self.buttonWindow1_onClick)
        self.lineEdit1 = QLineEdit("Type here what you want to transfer for [Window1].", self)
        self.lineEdit1.setGeometry(250, 100, 400, 30)

        buttonWindow2 = QPushButton('Window2', self)
        buttonWindow2.move(100, 200)
        buttonWindow2.clicked.connect(self.buttonWindow2_onClick)        
        self.lineEdit2 = QLineEdit("Type here what you want to transfer for [Window2].", self)
        self.lineEdit2.setGeometry(250, 200, 400, 30)
        self.show()

    @pyqtSlot()
    def buttonWindow1_onClick(self):
        self.statusBar().showMessage("Switched to window 1")
        self.cams = Window1(self.lineEdit1.text()) 
        self.cams.show()
        self.close()

    @pyqtSlot()
    def buttonWindow2_onClick(self):
        self.statusBar().showMessage("Switched to window 2")
        self.cams = Window2(self.lineEdit2.text()) 
        self.cams.show()
        self.close()


class Window1(QWindow):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Window1')
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))

        label1 = QLabel(value)
        self.button = QPushButton()
        self.button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.button.setIcon(self.style().standardIcon(QStyle.SP_ArrowLeft))
        self.button.setIconSize(QSize(200, 200))

        layoutV = QVBoxLayout()
        self.pushButton = QPushButton(self)
        self.pushButton.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
        self.pushButton.setText('Click me!')
        self.pushButton.clicked.connect(self.goMainWindow)
        layoutV.addWidget(self.pushButton)

        layoutH = QHBoxLayout()
        layoutH.addWidget(label1)
        layoutH.addWidget(self.button)
        layoutV.addLayout(layoutH)
        self.setLayout(layoutV)

    def goMainWindow(self):
        self.cams = Window()
        self.cams.show()
        self.close() 


class Window2(QDialog):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Window2')
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))

        label1 = QLabel(value)
        self.button = QPushButton()
        self.button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.button.setIcon(self.style().standardIcon(QStyle.SP_ArrowLeft))
        self.button.setIconSize(QSize(200, 200))

        layoutV = QVBoxLayout()
        self.pushButton = QPushButton(self)
        self.pushButton.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
        self.pushButton.setText('Click me!')
        self.pushButton.clicked.connect(self.goMainWindow)
        layoutV.addWidget(self.pushButton)

        layoutH = QHBoxLayout()
        layoutH.addWidget(label1)
        layoutH.addWidget(self.button)
        layoutV.addLayout(layoutH)
        self.setLayout(layoutV)

    def goMainWindow(self):
        self.cams = Window()
        self.cams.show()
        self.close()    


if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Window()
    sys.exit(app.exec_())