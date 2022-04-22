from distutils.command.clean import clean
from DataFetcher import DataFetcher
#from MainWindow import Ui_MainWindow
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Model:
    def __init__(self, datafetcher: DataFetcher):
        self.datafetcher = datafetcher 


    def fetch_realtime(self, start_date, end_date, table_variables, interval, aggregation):
        """
        Fetches realtime data from datafetcher, cleans the data and passes it on.
        """
        data = self.datafetcher.get_realtime(start_date, end_date, table_variables, interval, aggregation)
        if data.empty:
            return
        data = self.clean_data(data)
        return data
        
    def fetch_historical(self, years, categories):
        """
        Fetches historical data from datafetcher, cleans the data and passes it on.
        """

        data = self.datafetcher.get_historical(years, categories)
        if data.empty:
            return
        data = self.clean_data(data)
        return data


    def clean_data(self, df: pd.DataFrame):
        """
        Clear NaN's and null values from dataframe
        """
        df.fillna(method='ffill', inplace=True)
        df.fillna(method='bfill', inplace=True)
        df.fillna(0, inplace=True)
        return df