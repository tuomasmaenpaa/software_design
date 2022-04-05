from pathlib import Path

class Controller:
    def __init__(self, model):
        self.model = model

    def handle_realtime(self):
        pass

    def handle_historical(self):
        pass
    
    def save_historical_defaults(self, years, categories):
        pass

    def save_realtime_defaults(self, start_date, end_date, table_variables, interval, aggregation):
        pass
    