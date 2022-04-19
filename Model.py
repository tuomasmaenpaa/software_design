from distutils.command.clean import clean
from DataFetcher import DataFetcher
from MainWindow import Ui_MainWindow
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Model:
    def __init__(self, datafetcher: DataFetcher, ui: Ui_MainWindow):
        self.datafetcher = datafetcher 
        self.ui = ui

    def fetch_realtime(self, start_date, end_date, table_variables, interval, aggregation):
        data = self.datafetcher.get_realtime(start_date, end_date, table_variables, interval, aggregation)
        # TODO do something with the data, at the very least plot it in View

        if data.empty:
            return
        data = self.clean_data(data)
        self.plot_realtime(data)
        
    def fetch_historical(self, years, categories):
        data = self.datafetcher.get_historical(years, categories)
        # TODO do something with the data, at the very least plot it in View 
        
        if data.empty:
            return
        data = self.clean_data(data)
        self.plot_historical(data)


    def clean_data(self, df: pd.DataFrame):
        # Clear NaN's and null values from dataframe
        df.fillna(method='ffill', inplace=True)
        df.fillna(method='bfill', inplace=True)
        return df

    def plot_historical(self, data: pd.DataFrame):
        # TODO Some data might contain values 100 or 1000 times larger than others,
        #   making plots unreadable. Also the unit could be different so multiple y-axises needed?

        data.plot(ax=self.ui.graphWidget_2.canvas.ax)
        #self.ui.graphWidget.canvas.ax.plot([1,2,3,4],[1,2,3,4])
        return

    def plot_realtime(self, data: pd.DataFrame):
        
        data.plot(ax=self.ui.graphWidget.canvas.ax)
        return