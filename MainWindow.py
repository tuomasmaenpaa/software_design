# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from tracemalloc import start
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette, QFontMetrics, QStandardItem
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
import matplotlib

from pathlib import Path
import json
from Controller import Controller

path = Path(__file__).parent / 'opt' / 'simple_menu.json'
menu_f = open(path)
menu = json.load(menu_f)
menu_f.close()

gasList = ['CO\u2082', 'NO\u2093', 'SO\u2082']
path = Path(__file__).parent / 'opt' / 'hist.json'
hist_f = open(path, 'r')
hist = json.load(hist_f)
hist_f.close()


hist_list = list(hist.keys())

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1100, 700))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel('Center',self.tab)
        self.label.setGeometry(QtCore.QRect(300, 10, 171, 51))
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(30, 80, 1021, 61))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        #self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBoxStation = CheckableComboBox(self.frame)
        self.comboBoxStation.setGeometry(QtCore.QRect(20, 20, 104, 26))
        self.comboBoxStation.setObjectName("comboBoxStation")
        self.comboBoxStation.addItems(menu.keys())

        self.stationLabel1 = QtWidgets.QLabel('Station', self.tab)
        self.stationLabel1.setObjectName("stationLabel1")
        self.stationLabel1.setGeometry(QtCore.QRect(10, 75, 171, 30))
        self.stationLabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.gasLabel1 = QtWidgets.QLabel('Gas', self.tab)
        self.gasLabel1.setObjectName("gasLabel1")
        self.gasLabel1.setGeometry(QtCore.QRect(130, 80, 171, 20))
        self.gasLabel1.setAlignment(QtCore.Qt.AlignCenter)

        self.comboBoxGas = CheckableComboBox(self.frame)
        self.comboBoxGas.setGeometry(QtCore.QRect(140, 20, 104, 26))
        self.comboBoxGas.setObjectName("comboBoxGas")
        self.comboBoxGas.addItems(gasList)

        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.frame)
        self.dateTimeEdit.setGeometry(QtCore.QRect(260, 20, 110, 24))
        self.dateTimeEdit.setObjectName("dateTimeEdit")

        self.dateLabel1 = QtWidgets.QLabel('From', self.tab)
        self.dateLabel1.setObjectName('dateLabel1')
        self.dateLabel1.setGeometry(QtCore.QRect(250,80,171,20))
        self.dateLabel1.setAlignment(QtCore.Qt.AlignCenter)

        self.dateLabel2 = QtWidgets.QLabel('To', self.tab)
        self.dateLabel2.setObjectName('dateLabel2')
        self.dateLabel2.setGeometry(QtCore.QRect(370,80,171,20))
        self.dateLabel2.setAlignment(QtCore.Qt.AlignCenter)


        aggregations = ["NONE", "MIN", "MAX", "ARITHMETIC"]
        self.aggregationCheckBox = QtWidgets.QComboBox(self.frame)
        self.aggregationCheckBox.setGeometry(QtCore.QRect(490, 20, 104, 26))
        self.aggregationCheckBox.addItems(aggregations)


        self.aggLabel = QtWidgets.QLabel('Aggregation', self.tab)
        self.aggLabel.setObjectName('aggLabel')
        self.aggLabel.setGeometry(QtCore.QRect(480,80,171,20))
        self.aggLabel.setAlignment(QtCore.Qt.AlignCenter)

        botLimit = QDateTime(2013, 1, 1, 00, 00)
        topLimit = QDateTime.currentDateTime()

        self.dateTimeEdit.setDateTimeRange(botLimit, topLimit)
        self.dateTimeEdit1_2 = QtWidgets.QDateTimeEdit(self.frame)
        self.dateTimeEdit1_2.setGeometry(QtCore.QRect(380, 20, 110, 24))
        self.dateTimeEdit1_2.setObjectName("dateTimeEdit1_2")
        self.dateTimeEdit1_2.setDateTimeRange(botLimit, topLimit)
        
        self.intervalSpinBox = QtWidgets.QSpinBox(self.frame)
        self.intervalSpinBox.setMinimum(1)
        self.intervalSpinBox.setMaximum(60)
        self.intervalSpinBox.setGeometry(QtCore.QRect(600,20,50,24))

        self.spinLabel = QtWidgets.QLabel('Interval', self.tab)
        self.spinLabel.setObjectName('aggLabel')
        self.spinLabel.setGeometry(QtCore.QRect(590,73,171,30))
        self.spinLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.defaultCheck = QtWidgets.QCheckBox('Use defaults', self.frame)
        self.defaultCheck.setGeometry(QtCore.QRect(650,20,120,24))

        self.defaultSaveCheck = QtWidgets.QCheckBox('Save as defaults', self.frame)
        self.defaultSaveCheck.setGeometry(QtCore.QRect(750,20,120,24))


        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(890, 10, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.plot_realtime)

        self.graphWidget = MplWidget(self.tab)
        self.graphWidget.setGeometry(QtCore.QRect(30, 160, 1021, 441))
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

        self.gasLabel2 = QtWidgets.QLabel('Measurement', self.tab_2)
        self.gasLabel2.setObjectName("gasLabel2")
        self.gasLabel2.setGeometry(QtCore.QRect(130, 65, 171, 51))
        self.gasLabel2.setAlignment(QtCore.Qt.AlignCenter)

        self.comboBox_4 = CheckableComboBox(self.frame_2)
        self.comboBox_4.setGeometry(QtCore.QRect(20, 20, 200, 26))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItems(hist_list)

        botLimit2 = QDateTime(1975, 1, 1, 00, 00)
        topLimit2 = QDateTime(2017, 1, 1, 00, 00)

        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.frame_2)
        self.dateTimeEdit_2.setDisplayFormat("yyyy")
        self.dateTimeEdit_2.setDateTimeRange(botLimit2, topLimit2)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(300, 20, 110, 24))
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 10, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.plot_historical)

        self.dateTimeEdit_3 = QtWidgets.QDateTimeEdit(self.frame_2)
        self.dateTimeEdit_3.setDisplayFormat("yyyy")
        self.dateTimeEdit_3.setGeometry(QtCore.QRect(430, 20, 110, 24))
        self.dateTimeEdit_3.setObjectName("dateTimeEdit_3")
        self.dateTimeEdit_3.setDateTimeRange(botLimit2, topLimit2)
        
        self.graphWidget_2 = MplWidget(self.tab_2)
        self.graphWidget_2.setGeometry(QtCore.QRect(30, 160, 1021, 441))
        self.graphWidget_2.setObjectName("graphWidget_2")
        
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        
        self.tab_3.setObjectName("tab_3")
       
        self.label_3 = QtWidgets.QLabel('Center', self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(260, 10, 251, 20))
        self.label_3.setObjectName("label_3")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)

        self.graphComparison = MplWidgetDouble(self.tab_3)
        self.graphComparison.setGeometry(QtCore.QRect(30, 30, 1021, 621))
        self.graphComparison.setObjectName("graphComparison")

        self.tabWidget.addTab(self.tab_3, "")
    #    self.tab_4 = QtWidgets.QWidget()
    #    self.tab_4.setObjectName("tab_4")
    #    self.tabWidget.addTab(self.tab_4, "")
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

        self.controller = ''

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "View Real Time Data"))

        self.pushButton.setText(_translate("MainWindow", "Plot"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Real-Time"))
        self.label_2.setText(_translate("MainWindow", "View Historical Data"))

        self.pushButton_2.setText(_translate("MainWindow", "Plot"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Historical"))

        self.label_3.setText(_translate("MainWindow", "Compare Historical and Real-Time Data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Compare"))
       # self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Averages"))
    
    def setup_controller(self, controller: Controller):
        self.controller = controller

    def plot_realtime(self):

        use_defaults = self.defaultCheck.isChecked()
        save_defaults = self.defaultSaveCheck.isChecked()

        if use_defaults:
            data = self.controller.handle_realtime(use_defaults=use_defaults, save_defaults=save_defaults)
        else:
            stations = self.comboBoxStation.currentData()
            gases = self.comboBoxGas.currentData()

            table_variables = self.controller.get_tablevariables(stations, gases)

            if len(table_variables) == 0:
                return

            start_date = self.dateTimeEdit.dateTime()
            end_date = self.dateTimeEdit1_2.dateTime()

            # If the user selects the end date to be before start date, flip them around.
            # If the datetimes are the same, add a day to end date.
            if end_date < start_date:
                temp = end_date
                end_date = start_date
                start_date = temp
            elif end_date == start_date:
                end_date.addDays(1)


            start_date = self.controller.datetime_to_ISO_string(start_date)
            end_date = self.controller.datetime_to_ISO_string(end_date)
            try:
                aggregation = str(self.aggregationCheckBox.currentText())
            except:
                aggregation = 'NONE'
            interval = '30'

            data = self.controller.handle_realtime(start_date=start_date, end_date=end_date, table_variables=table_variables,
                    interval=interval, aggregation=aggregation, use_defaults=use_defaults, save_defaults=save_defaults)
        
        # Clear previous plots
        self.graphWidget.canvas.ax.cla()
        data.plot(ax=self.graphWidget.canvas.ax)
        self.graphWidget.canvas.draw()

        self.graphComparison.canvas.ax.cla()
        data.plot(ax=self.graphComparison.canvas.ax)
        self.graphComparison.canvas.draw()

    def plot_historical(self):

        start_year = self.controller.get_year(self.dateTimeEdit_2.date())
        end_year = self.controller.get_year(self.dateTimeEdit_3.date())
        years = list(range(start_year, end_year))

        measurements = self.comboBox_4.currentData()
        categories = [hist[m] for m in measurements]

        

        data = self.controller.handle_historical(years=years, categories=categories, use_defaults=False, save_defaults=False)
        self.graphWidget_2.canvas.ax.cla()
        data.plot(ax=self.graphWidget_2.canvas.ax)
        self.graphWidget_2.canvas.draw()

        # We plot the same plot for the comparison tab
        self.graphComparison.canvas.ax2.cla()
        data.plot(ax=self.graphComparison.canvas.ax2)
        self.graphComparison.canvas.draw()


    

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

# Matplotlib canvas class to create figure
class MplCanvasDouble(Canvas):
    def __init__(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(211)
        self.ax2 = self.fig.add_subplot(212)
        Canvas.__init__(self, self.fig)
        Canvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        Canvas.updateGeometry(self)

# Matplotlib widget
class MplWidgetDouble(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)   # Inherit from QWidget
        self.canvas = MplCanvasDouble()                  # Create canvas object
        self.vbl = QtWidgets.QVBoxLayout()         # Set box for plotting
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)



class CheckableComboBox(QtWidgets.QComboBox):

    # Subclass Delegate to increase item height
    class Delegate(QtWidgets.QStyledItemDelegate):
        def sizeHint(self, option, index):
            size = super().sizeHint(option, index)
            size.setHeight(20)
            return size

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Make the combo editable to set a custom text, but readonly
        self.setEditable(True)
        self.lineEdit().setReadOnly(True)

        # Use custom delegate
        self.setItemDelegate(CheckableComboBox.Delegate())

        # Update the text when an item is toggled
        self.model().dataChanged.connect(self.updateText)

        # Hide and show popup when clicking the line edit
        self.lineEdit().installEventFilter(self)
        self.closeOnLineEditClick = False

        # Prevent popup from closing when clicking on an item
        self.view().viewport().installEventFilter(self)

    def loadGases(self, event):
        # TODO GASES TO COMBOBOX
        return

    def resizeEvent(self, event):
        # Recompute text to elide as needed
        self.updateText()
        super().resizeEvent(event)

    def eventFilter(self, object, event):

        if object == self.lineEdit():
            if event.type() == QtCore.QEvent.MouseButtonRelease:
                if self.closeOnLineEditClick:
                    self.hidePopup()
                else:
                    self.showPopup()
                return True
            return False

        if object == self.view().viewport():
            if event.type() == QtCore.QEvent.MouseButtonRelease:
                index = self.view().indexAt(event.pos())
                item = self.model().item(index.row())

                if item.checkState() == QtCore.Qt.Checked:
                    item.setCheckState(QtCore.Qt.Unchecked)
                else:
                    item.setCheckState(QtCore.Qt.Checked)
                return True
        return False

    def showPopup(self):
        super().showPopup()
        # When the popup is displayed, a click on the lineedit should close it
        self.closeOnLineEditClick = True

    def hidePopup(self):
        super().hidePopup()
        # Used to prevent immediate reopening when clicking on the lineEdit
        self.startTimer(100)
        # Refresh the display text when closing
        self.updateText()

    def timerEvent(self, event):
        # After timeout, kill timer, and reenable click on line edit
        self.killTimer(event.timerId())
        self.closeOnLineEditClick = False

    def updateText(self):
        texts = []
        for i in range(self.model().rowCount()):
            if self.model().item(i).checkState() == QtCore.Qt.Checked:
                texts.append(self.model().item(i).text())
        text = ", ".join(texts)

        # Compute elided text (with "...")
        metrics = QFontMetrics(self.lineEdit().font())
        elidedText = metrics.elidedText(text, QtCore.Qt.ElideRight, self.lineEdit().width())
        self.lineEdit().setText(elidedText)

    def addItem(self, text, data=None):
        item = QStandardItem()
        item.setText(text)
        if data is None:
            item.setData(text)
        else:
            item.setData(data)
        item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable)
        item.setData(QtCore.Qt.Unchecked, QtCore.Qt.CheckStateRole)
        self.model().appendRow(item)

    def addItems(self, texts, datalist=None):
        for i, text in enumerate(texts):
            try:
                data = datalist[i]
            except (TypeError, IndexError):
                data = None
            self.addItem(text, data)

    def currentData(self):
        # Return the list of selected items data
        res = []
        for i in range(self.model().rowCount()):
            if self.model().item(i).checkState() == QtCore.Qt.Checked:
                res.append(self.model().item(i).data())
        return res

