from DataFetcher import DataFetcher
from MainWindow import Ui_MainWindow
import pandas as pd
import numpy as np

class Model:
    def __init__(self, datafetcher: DataFetcher, ui: Ui_MainWindow):
        self.datafetcher = datafetcher 
        self.ui = ui

    def fetch_realtime(self, start_date, end_date, table_variables, interval, aggregation):
        data = self.datafetcher.get_realtime(start_date, end_date, table_variables, interval, aggregation)
        # TODO do something with the data, at the very least plot it in View

    def fetch_historical(self, years, categories):
        data = self.datafetcher.get_historical(years, categories)
        # TODO do something with the data, at the very least plot it in View 

    # TODO 