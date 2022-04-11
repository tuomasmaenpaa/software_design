from pathlib import Path
import json

from Model import Model

class Controller:
    def __init__(self, model: Model):
        self.model = model

    def handle_realtime(self, use_defaults=True, save_defaults=False):

        if use_defaults:
            path = Path(__file__).parent / "realtime_default.json"
            with open(path, 'r') as infile:
                defaults = json.load(infile)
                self.model.fetch_realtime(defaults['start_date'], 
                defaults['end_date'], defaults['table_variables'],
                defaults['interval'], defaults['aggregation'])

        

    def handle_historical(self, use_defaults=True, save_defaults=False):


        if use_defaults:
            path = Path(__file__).parent / "realtime_default.json"
            with open(path, 'r') as infile:
                defaults = json.load(infile)
                self.model.fetch_historical(defaults['years'], defaults['categories'])
    
    def save_historical_defaults(self, years, categories):

        path = Path(__file__).parent / "hist_default.json"
        defaults = {}
        defaults['years'] = years
        defaults['categories'] = categories
        
        with open(path, 'w') as outfile:
            json.dump(defaults, outfile)

        

    def save_realtime_defaults(self, start_date, end_date, table_variables, interval, aggregation):
        
        path = Path(__file__).parent / "realtime_default.json"
        defaults = {}
        defaults['start_date'] = start_date
        defaults['end_date'] = end_date
        defaults['table_variables'] = table_variables
        defaults['interval'] = interval
        defaults['aggregation'] = aggregation
        
        with open(path, 'w') as outfile:
            json.dump(defaults, outfile)
    