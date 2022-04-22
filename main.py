"""
Running this script initializes the program
"""

from Controller import Controller
from DataFetcher import DataFetcher
from Model import Model
from MainWindow import Ui_MainWindow

from PyQt5 import QtWidgets

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

    MainWindow.show()
    sys.exit(app.exec_())