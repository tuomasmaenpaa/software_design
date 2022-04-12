from pathlib import Path
import json
from datetime import datetime
from PyQt5 import QtCore
from Model import Model

class Controller:
    def __init__(self, model: Model):
        self.model = model

    def handle_realtime(self, use_defaults=True, save_defaults=False):

        if use_defaults:
            path = Path(__file__).parent / 'opt' / 'realtime_default.json'
            with open(path, 'r') as infile:
                defaults = json.load(infile)
                self.model.fetch_realtime(defaults['start_date'], 
                defaults['end_date'], defaults['table_variables'],
                defaults['interval'], defaults['aggregation'])

        

    def handle_historical(self, use_defaults=True, save_defaults=False):

        if use_defaults:
            path = Path(__file__).parent / 'opt' / 'hist_default.json'
            with open(path, 'r') as infile:
                defaults = json.load(infile)
                self.model.fetch_historical(defaults['years'], defaults['categories'])
    
    def save_historical_defaults(self, years, categories):
        """
        Save historical preferences to a file
        """
        path = Path(__file__).parent / 'opt' / 'hist_default.json'
        defaults = {}
        defaults['years'] = years
        defaults['categories'] = categories
        
        with open(path, 'w') as outfile:
            json.dump(defaults, outfile)

        

    def save_realtime_defaults(self, start_date, end_date, table_variables, interval, aggregation):

        """
        Save realtime preferences to a file 
        """
        
        path = Path(__file__).parent / 'opt' / 'realtime_default.json'
        defaults = {}
        defaults['start_date'] = start_date
        defaults['end_date'] = end_date
        defaults['table_variables'] = table_variables
        defaults['interval'] = interval
        defaults['aggregation'] = aggregation
        
        with open(path, 'w') as outfile:
            json.dump(defaults, outfile)
    
    def create_ISO_timestamp(self, date: QtCore.QDate):
        """
        Takes a QDate object and returns an ISO formatted timestamp for realtime API calls
        """
        year, month, day = date.getDate()
        hour, minute, second, millisecond = 12, 0, 0, 0
        iso_date = datetime(year, month, day, hour, minute, second, millisecond)
        return iso_date.isoformat(timespec='milliseconds')
        