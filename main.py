"""
Running this script initializes the program
"""

from Controller import Controller
from DataFetcher import DataFetcher
from Model import Model
from MainWindow import Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
import matplotlib

if __name__ == "__main__":


    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    dataf = DataFetcher()
    model = Model(dataf)
    controller = Controller(model)
    ui.setup_controller(controller)
    ui.plot_realtime()
    ui.plot_historical()
    ui.plot_comparison()
    #controller.handle_historical(True, False)
    #controller.handle_realtime(True, False)
    MainWindow.show()
    sys.exit(app.exec_())