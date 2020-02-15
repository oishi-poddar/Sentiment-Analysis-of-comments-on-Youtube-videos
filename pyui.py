from CommentsTesting import YouTubeApi
from data_clean import CleanAndTest

import sys

from PyQt5 import QtGui

from PyQt5.QtGui import QIcon, QPixmap

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QWidget, QAction, QMessageBox, \
    QPushButton, QLineEdit, QLabel


class Window(QMainWindow):

    def InitWindow(self):
        mainMenu = self.menuBar()

        aboutmenu = mainMenu.addMenu("About")

        aboutUs = QAction(QIcon("youtube.png"), "About Us", self)

        aboutUs.setShortcut("Ctrl+A")

        aboutUs.setStatusTip("Want to know more?")

        aboutUs.triggered.connect(self.AboutUs)

        aboutmenu.addAction(aboutUs)

        self.setWindowTitle(self.title)

        self.setGeometry(self.top, self.left, self.width, self.height)

        self.statusBar().showMessage("Made in love with Python")

        self.show()

    # def CloseApp(self):

    #     reply = QMessageBox.question(self,"Alert","Are you sure you want to close?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

    #     if reply == QMessageBox.Yes:

    #         self.close()

    def AboutUs(self):
        QMessageBox.about(self, "About the application",
                          "This application analyses users' sentiments about a video using youtube comments")

    def onClick(self):
        url = self.lineEdit.text()

        l1 = url.rsplit('=', 1)

        print(l1[-1])

        y = YouTubeApi()

        t = y.get_video_comment(l1[-1])

        CleanAndTest.filter_data(self)

        print(t)

        # yy= Datac()

        # tt=yy.piechart()

        self.label2 = QLabel(self)

        self.label2.setPixmap(QPixmap('pie.png'))

        self.label2.setGeometry(300, 150, 1500, 500)

        self.label2.show()

    def __init__(self):
        super().__init__()

        self.title = "Youtube Comment Analyser"

        self.top = 00

        self.left = 30

        self.width = 1550

        self.height = 720

        self.setWindowIcon(QtGui.QIcon("youtube.png"))

        self.lineEdit = QLineEdit(self)

        self.lineEdit.move(500, 50)

        self.lineEdit.resize(300, 30)

        self.label1 = QLabel("Enter URL:", self)

        self.label1.move(400, 50)

        newFont = QtGui.QFont("Times", 12, QtGui.QFont.Bold)

        self.label1.setFont(newFont)

        button3 = QPushButton("Analyse", self)

        button3.move(800, 50)

        button3.setToolTip("<h4>Know more</h4>")

        button3.clicked.connect(self.onClick)

        self.InitWindow()


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())








