from pathlib import Path
import json
from datetime import datetime
from PyQt5 import QtCore
from numpy import save
from Model import Model

class Controller:
    def __init__(self, model: Model):
        self.model = model

    def handle_realtime(self, start_date='', end_date='', table_variables=[], interval='', 
                        aggregation='', use_defaults=True, save_defaults=False): 
        """
        Retrieves data based on user selection
        """

        # We only save new defaults if we are using new values, not the old defaults       
        if save_defaults & (not use_defaults):
            self.save_realtime_defaults(start_date, end_date, table_variables,
            interval, aggregation)

        if use_defaults:
            path = Path(__file__).parent / 'opt' / 'realtime_default.json'
            with open(path, 'r') as infile:
                defaults = json.load(infile)
                infile.close()
                return self.model.fetch_realtime(defaults['start_date'], 
                        defaults['end_date'], defaults['table_variables'],
                        defaults['interval'], defaults['aggregation'])
        else:
            return self.model.fetch_realtime(start_date, end_date, table_variables,
                    interval, aggregation)
        

    def handle_historical(self, years=[], categories=[], use_defaults=True, save_defaults=False):
        """
        Retrieves data based on user selection
        """

        if save_defaults & (not use_defaults):
            self.save_historical_defaults(years, categories)
            
        if use_defaults:
            path = Path(__file__).parent / 'opt' / 'hist_default.json'
            with open(path, 'r') as infile:
                defaults = json.load(infile)
                infile.close()
                return self.model.fetch_historical(defaults['years'], defaults['categories'])
        else:
            return self.model.fetch_historical(years, categories)    


    def save_historical_defaults(self, years: list, categories: list):
        """
        Save historical preferences to a file
        """
        path = Path(__file__).parent / 'opt' / 'hist_default.json'
        defaults = {}
        defaults['years'] = years
        defaults['categories'] = categories
        
        with open(path, 'w') as outfile:
            json.dump(defaults, outfile)

        

    def save_realtime_defaults(self, start_date: str, end_date: str, table_variables: list, 
        interval: str, aggregation: str):

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
    
    def get_year(self, date: QtCore.QDate):
        """
        Takes a QDate object and returns an ISO formatted timestamp for realtime API calls
        """
        year, month, day = date.getDate()
        return year
    
    def datetime_to_ISO_string(self, date: QtCore.QDateTime):
        """
        Takes a QDateTime object and returns an ISO formatted timestamp for API calls
        """
        return date.toPyDateTime().isoformat(timespec='milliseconds')
    
    def get_tablevariables(self, stations: list, variables: list):
        """
        Returns a list of tablevariables for given list of gases for given list of stations
        """

        menu = open('opt/simple_menu.json', 'r')
        menu = json.load(menu)

        tv = []
        for s in stations:
            for v in variables:
                try:
                    tv.append(menu[s]['variables'][v])
                except KeyError:
                    pass
        return tv

    def generate_filepath(self, source):
        """
        Generate filepath for figure, source is realtime, historical or compare
        """
        now = datetime.now().isoformat()
        name = source + '_' + now + '.png'
        path = Path(__file__).parent / 'figures' / name
        return path
