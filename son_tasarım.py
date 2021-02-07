# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 20:25:09 2021

@author: yazılım
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import time
from PyQt5 import QtWidgets,uic,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QTextBrowser, QPushButton, QVBoxLayout, QProgressBar,QComboBox
from elektrikli_araba_python import Ui_MainWindow
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtGui import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from PyQt5.uic import loadUi

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
import numpy as np

def ceviriProgramim():

    class MainWindow(QMainWindow):
        def __init__(self):
            super(MainWindow, self).__init__()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            #Butonları tanımlama
            self.setStyleSheet("background-color: rgb(61, 68,149);")

            self.ui.pushButton_7.setVisible(False)
            self.ui.pushButton_8.setVisible(False)
            self.ui.pushButton_9.setVisible(False)
            self.ui.pushButton_10.setVisible(False)
            self.ui.pushButton_11.setVisible(False)
            self.ui.pushButton_12.setVisible(False)

            self.ui.pushButton.clicked.connect(self.button_clicked_slot)
            self.ui.pushButton_2.clicked.connect(self.button_2clicked_slot)
            self.ui.pushButton_3.clicked.connect(self.button_3clicked_slot)
            self.ui.pushButton_4.clicked.connect(self.button_4clicked_slot)
            self.ui.pushButton_5.clicked.connect(self.button_5clicked_slot)
            self.ui.pushButton_6.clicked.connect(self.button_6clicked_slot)
            self.ui.pushButton_7.clicked.connect(self.button_7clicked_slot)
            self.ui.pushButton_8.clicked.connect(self.button_8clicked_slot)
            self.ui.pushButton_9.clicked.connect(self.button_9clicked_slot)
            self.ui.pushButton_10.clicked.connect(self.button_10clicked_slot)
            self.ui.pushButton_11.clicked.connect(self.button_11clicked_slot)
            self.ui.pushButton_12.clicked.connect(self.button_12clicked_slot)

            # renkler
            self.ui.pushButton.setStyleSheet("background-color: rgb(115, 196,200);")
            #self.ui.pushButton.setIcon(QIcon("buton.png"))
            self.ui.pushButton_2.setStyleSheet("background-color: rgb(115, 196,200);")
            self.ui.pushButton_3.setStyleSheet("background-color: rgb(115, 196,200);")
            self.ui.pushButton_4.setStyleSheet("background-color: rgb(115, 196,200);")
            self.ui.pushButton_5.setStyleSheet("background-color: rgb(115, 196,200);")
            self.ui.pushButton_6.setStyleSheet("background-color: rgb(115, 196,200);")
            self.ui.pushButton_7.setStyleSheet("background-color: rgb(115, 196,200);")
            self.ui.pushButton_8.setStyleSheet("background-color: rgb(115, 196,200);")
            self.ui.pushButton_9.setStyleSheet("background-color: rgb(115, 196,200);")
            self.ui.pushButton_10.setStyleSheet("background-color: rgb(115, 196,200);")
            self.ui.pushButton_11.setStyleSheet("background-color: rgb(115, 196,200);")
            self.ui.pushButton_12.setStyleSheet("background-color: rgb(115, 196,200);")
        def button_3clicked_slot(self):
            print("bays kapattım")
            self.close()
        def button_clicked_slot(self):
            print("button_clicked_slot")
            
            #GPIO.cleanup()
            #GPIO.setmode(#GPIO.BOARD)
            #GPIO.setup(3, #GPIO.OUT)
            #GPIO.output(3, #GPIO.HIGH)
            self.ui.pushButton.setVisible(False)
            self.ui.pushButton_11.setVisible(True)
        def button_2clicked_slot(self):
            print("button_2clicked_slot")
            #GPIO.cleanup()
            #GPIO.setmode(#GPIO.BOARD)
            #GPIO.setup(5, #GPIO.OUT)
            #GPIO.output(5, #GPIO.HIGH)

            self.ui.pushButton_2.setVisible(False)
            self.ui.pushButton_7.setVisible(True)

        def button_4clicked_slot(self):
            print("button_4clicked_slot")
            #GPIO.cleanup()
            #GPIO.setmode(#GPIO.BOARD)
            #GPIO.setup(11, #GPIO.OUT)
            #GPIO.output(11, #GPIO.HIGH)


            self.ui.pushButton_4.setVisible(False)
            self.ui.pushButton_9.setVisible(True)
        def button_5clicked_slot(self):
            print("button_5clicked_slot")
            #GPIO.cleanup()
            #GPIO.setmode(#GPIO.BOARD)
            #GPIO.setup(13, #GPIO.OUT)
            #GPIO.output(13, #GPIO.HIGH)


            self.ui.pushButton_5.setVisible(False)
            self.ui.pushButton_10.setVisible(True)
        def button_6clicked_slot(self):
            print("button_6clicked_slot")
            #GPIO.cleanup()
            #GPIO.setmode(#GPIO.BOARD)
            #GPIO.setup(15, #GPIO.OUT)
            #GPIO.output(15, #GPIO.HIGH)

            self.ui.pushButton_6.setVisible(False)
            self.ui.pushButton_8.setVisible(True)

        def button_7clicked_slot(self):
            print("hello7")

            #GPIO.cleanup()
            #GPIO.setmode(#GPIO.BOARD)
            #GPIO.setup(5, #GPIO.OUT)
            #GPIO.output(5, #GPIO.LOW)

            self.ui.pushButton_7.setVisible(False)
            self.ui.pushButton_2.setVisible(True)
        def button_8clicked_slot(self):
            print("hello8")

            #GPIO.setmode(#GPIO.BOARD)
            #GPIO.setup(7, #GPIO.OUT)
            #GPIO.output(7, #GPIO.LOW)
            self.ui.pushButton_8.setVisible(False)
            self.ui.pushButton_6.setVisible(True)
        def button_9clicked_slot(self):
            print("hello9")
            #GPIO.cleanup()
            #GPIO.setmode(#GPIO.BOARD)
            #GPIO.setup(11, #GPIO.OUT)
            #GPIO.output(11, #GPIO.LOW)
            self.ui.pushButton_9.setVisible(False)
            self.ui.pushButton_4.setVisible(True)
        def button_10clicked_slot(self):
            print("hello10")

            #GPIO.setmode(#GPIO.BOARD)
            #GPIO.setup(13, #GPIO.OUT)
            #GPIO.output(13, #GPIO.LOW)
            self.ui.pushButton_10.setVisible(False)
            self.ui.pushButton_5.setVisible(True)
        def button_11clicked_slot(self):
            print("hello11")
            #GPIO.cleanup()
            #GPIO.setmode(#GPIO.BOARD)
            #GPIO.setup(3, #GPIO.OUT)
            #GPIO.output(3, #GPIO.LOW)
            self.ui.pushButton_11.setVisible(False)
            self.ui.pushButton.setVisible(True)
        def button_12clicked_slot(self):
            print("helloaaa12")
            #GPIO.cleanup()
            #GPIO.setmode(#GPIO.BOARD)
            #GPIO.setup(7, #GPIO.OUT)
            #GPIO.output(7, #GPIO.LOW)
            self.ui.pushButton_12.setVisible(False)
            self.ui.pushButton_3.setVisible(True)
            
    if __name__ == "__main__":
        app = QApplication(sys.argv)

        window = MainWindow()
        window.setWindowTitle("Batuhan ökmen")
        #window.showFullScreen()
        window.show()

        sys.exit(app.exec_())

ceviriProgramim()