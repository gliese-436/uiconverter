#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
from PyQt5.QtWidgets import (QMainWindow, QLabel,
    QAction, QFileDialog, QLineEdit, QApplication, QPushButton)
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        
        
        self.statusBar()
        self.setWindowIcon(QIcon('icon.png')) 
        btn1 = QPushButton("Выбрать", self)
        btn1.move(20, 100)
        btn1.clicked.connect(self.showDialog)

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Введите имя для .py файла')
        self.nameLabel.move(20, 20)
        self.nameLabel.resize(200, 32)

        self.line = QLineEdit(self)
        self.line.move(20, 50)
        self.line.resize(200, 32)

        self.setGeometry(100, 100, 250, 200)
        self.setWindowTitle('.ui в .py')
        self.show()


    def showDialog(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]

        f = open(fname, 'r')

        with f:
            pyname = self.line.text()
            uiname = str(os.path.basename(fname))[0:-3]
            if pyname == '': pyname = uiname
            os.popen("pyuic5 {0}.ui -o {1}.py".format(uiname, pyname) )
            self.statusBar().showMessage('готово!')
        


if __name__ == '__main__':


    app = QApplication(sys.argv)
    ex = Example()
    ex.setStyleSheet("background: #c6f2da")
    sys.exit(app.exec_())