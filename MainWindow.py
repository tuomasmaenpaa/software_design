# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
import matplotlib
#from mplwidget import MplWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 781, 541))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel('Center',self.tab)
        self.label.setGeometry(QtCore.QRect(300, 10, 171, 51))
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(30, 80, 721, 61))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(20, 20, 104, 26))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(140, 20, 104, 26))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.dateEdit = QtWidgets.QDateEdit(self.frame)
        self.dateEdit.setGeometry(QtCore.QRect(300, 20, 110, 24))
        self.dateEdit.setObjectName("dateEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(590, 10, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.graphWidget = MplWidget(self.tab)
        self.graphWidget.setGeometry(QtCore.QRect(30, 160, 721, 341))
        self.graphWidget.setObjectName("graphWidget")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_2 = QtWidgets.QLabel('Center', self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(300, 10, 171, 51))
        self.label_2.setObjectName("label_2")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.frame_2 = QtWidgets.QFrame(self.tab_2)
        self.frame_2.setGeometry(QtCore.QRect(30, 80, 721, 61))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_3.setGeometry(QtCore.QRect(20, 20, 104, 26))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_4.setGeometry(QtCore.QRect(140, 20, 104, 26))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.frame_2)
        self.dateEdit_2.setGeometry(QtCore.QRect(300, 20, 110, 24))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 10, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.dateEdit_3 = QtWidgets.QDateEdit(self.frame_2)
        self.dateEdit_3.setGeometry(QtCore.QRect(430, 20, 110, 24))
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.graphWidget_2 = MplWidget(self.tab_2)
        self.graphWidget_2.setGeometry(QtCore.QRect(30, 160, 721, 341))
        self.graphWidget_2.setObjectName("graphWidget_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.frame_3 = QtWidgets.QFrame(self.tab_3)
        self.frame_3.setGeometry(QtCore.QRect(30, 80, 721, 61))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.comboBox_5 = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_5.setGeometry(QtCore.QRect(20, 20, 104, 26))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_6 = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_6.setGeometry(QtCore.QRect(140, 20, 104, 26))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.dateEdit_4 = QtWidgets.QDateEdit(self.frame_3)
        self.dateEdit_4.setGeometry(QtCore.QRect(300, 20, 110, 24))
        self.dateEdit_4.setObjectName("dateEdit_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_3.setGeometry(QtCore.QRect(590, 10, 113, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.dateEdit_5 = QtWidgets.QDateEdit(self.frame_3)
        self.dateEdit_5.setGeometry(QtCore.QRect(430, 20, 110, 24))
        self.dateEdit_5.setObjectName("dateEdit_5")
        self.label_3 = QtWidgets.QLabel('Center', self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(260, 10, 251, 51))
        self.label_3.setObjectName("label_3")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.graphWidget_3 = MplWidget(self.tab_3)
        self.graphWidget_3.setGeometry(QtCore.QRect(30, 160, 721, 341))
        self.graphWidget_3.setObjectName("graphWidget_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "View Real Time Data"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Station"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Gas"))
        self.pushButton.setText(_translate("MainWindow", "Plot"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Real-Time"))
        self.label_2.setText(_translate("MainWindow", "View Historical Data"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Station"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Gas"))
        self.pushButton_2.setText(_translate("MainWindow", "Plot"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Historical"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "Station"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "Gas"))
        self.pushButton_3.setText(_translate("MainWindow", "Plot"))
        self.label_3.setText(_translate("MainWindow", "Compare Historical and Real-Time Data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Compare"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Averages"))

# Ensure using PyQt5 backend
matplotlib.use('QT5Agg')

# Matplotlib canvas class to create figure
class MplCanvas(Canvas):
    def __init__(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        Canvas.__init__(self, self.fig)
        Canvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        Canvas.updateGeometry(self)

# Matplotlib widget
class MplWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)   # Inherit from QWidget
        self.canvas = MplCanvas()                  # Create canvas object
        self.vbl = QtWidgets.QVBoxLayout()         # Set box for plotting
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

