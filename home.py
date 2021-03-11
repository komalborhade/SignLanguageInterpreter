# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(558, 346)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 255);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 10, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 50, 161, 261))
        self.frame.setStyleSheet(_fromUtf8("background-color: rgb(203, 203, 203);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(30, 40, 99, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 110, 99, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 190, 99, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 70, 191, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.listView = QtGui.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(240, 101, 281, 211))
        self.listView.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.listView.setObjectName(_fromUtf8("listView"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Hand Talk Assitive", None))
        self.pushButton.setText(_translate("MainWindow", "Start", None))
        self.pushButton_2.setText(_translate("MainWindow", "Stop", None))
        self.pushButton_3.setText(_translate("MainWindow", "Exit", None))
        self.label_2.setText(_translate("MainWindow", "Gesture Detected", None))

