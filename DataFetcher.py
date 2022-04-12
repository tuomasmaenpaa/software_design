import requests
import json
from pathlib import Path
import pandas as pd
import numpy as np
from io import StringIO



class DataFetcher:
    def __init__(self):
        self.hist_options = self.__init_hist_options()
        self.realtime_options = self.__init_realtime_options()

    def __init_hist_options(self):
        """
        Private function to be used in finding the historical data limits
        """
        limits = self.__get_historical_limits()

        titles = limits['variables'][0]['valueTexts']
        keys = limits['variables'][0]['values']
        years = limits['variables'][1]['values']

        # Create a dict where the labels and years are easily accessible
        # First, find relevant categories i.e. Greenhouse gas statistics

        indices = [i for i, s in enumerate(titles) if 'reenhouse' in s]

        titles = [titles[i] for i in indices]
        keys = [keys[i] for i in indices]

        options = {}
        categories = {}
        # Fill  categories first
        for i in range(len(titles)):
            categories[titles[i]] = keys[i]

        options['categories'] = categories
        options['timerange'] = years
        return options

    def __init_realtime_options(self):
        options = {}

        stations = self.__get_stations()


        for station, station_id in stations:

            options[station] = {'id': station_id}
            options[station]['tables'] = {}
            tables = self.__get_smear_station_tables(station_id)

            for table, table_id in tables:

                options[station]['tables'][table] = {'table_id': table_id}
                options[station]['tables'][table]['variables'] = {}
                
                variables = self.__get_smear_station_table_variables(station_id, table_id)

                for variable, variable_id in variables:

                    options[station]['tables'][table]['variables'][variable] = variable_id

        return options

    def get_historical(self, years = [], categories = ["Khk_yht", "Khk_yht_index", "Khk_yht_las", "Khk_yht_las_index"]):
        """
        Returns a JSON of data from STATFI based on given parameters
        """
        path = Path(__file__).parent / 'opt' / 'request.json'

        url = 'https://pxnet2.stat.fi/PXWeb/api/v1/en/ymp/taulukot/Kokodata.px'
        payload = open(path)
        payload = json.load(payload)

        payload['query'][0]['selection']['values'] = categories
        payload['query'][1]['selection']['values'] = years

        payload = json.dumps(payload)

        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        res = requests.post(url, data=payload, headers=headers)

        return self.__hist_to_dataframe(json.loads(res.text))

    def get_realtime(self, start_date, end_date, table_variables, interval, aggregation):
        """
        Returns a JSON of data from SMEAR based on the parameters
        """

        url = 'https://smear-backend.rahtiapp.fi/search/timeseries/csv?'
        url += 'aggregation=' + aggregation
        url += '&interval=' + str(interval)
        url += '&from=' + start_date
        url += '&to=' + end_date

        for t_v in table_variables:
            url += '&tablevariable=' + t_v
        res = requests.get(url)

        data = pd.read_csv(StringIO(res.text))
        data['Datetime'] = pd.to_datetime(data[['Year','Month','Day','Hour','Minute','Second']])
        data.drop(['Year','Month','Day','Hour','Minute','Second'], axis=1, inplace=True)

        # Rearrange columns, Datetime first
        cols = data.columns.tolist()
        cols = cols[-1:] + cols[:-1]
        data = data[cols]
        data.set_index('Datetime', inplace=True)

        # Fix column names
        path = Path(__file__).parent / 'opt' / 'gases.json'
        gases = json.load(open(path, 'r'))
        data.rename(columns=gases, inplace=True)
        return data 
    
    def __get_stations(self):
        """
        Returns a list of tuples (station, id) of all available SMEAR API stations
        """
        res = requests.get('https://smear-backend.rahtiapp.fi/search/station')
        p = json.loads(res.text)

        stations = [(p[i]['name'], str(p[i]['id'])) for i in range(len(p)) ]
        return stations

    def __get_smear_station_tables(self, station_id):
        """
        Returns a list of tuples (name, id) of variable tables for station id
        """
        url = 'https://smear-backend.rahtiapp.fi/station/' + station_id + '/table'
        res = requests.get(url)
        p = json.loads(res.text)

        tables = [(p[i]['name'], str(p[i]['id'])) for i in range(len(p)) ]

        return tables   

    def __get_smear_station_table_variables(self, station_id, table_id):

        """
        Returns a list of tuples (name, id) of variable tables for station id
        """
        url = 'https://smear-backend.rahtiapp.fi/station/' + station_id + '/table/' + table_id + '/variable'
        res = requests.get(url)
        p = json.loads(res.text)

        variables = [(p[i]['name'], str(p[i]['id'])) for i in range(len(p))]

        return variables
 
    def __get_historical_limits(self):
        """
        Get the years and categories from which historical data can be used
        """
        res = requests.get('https://pxnet2.stat.fi/PXWeb/api/v1/en/ymp/taulukot/Kokodata.px')
        return json.loads(res.text)
    
    def __hist_to_dataframe(self, hist):
        n_years = hist['size'][1]
        # TODO CHANCGED KEYS TO VALUES FOR CATEGORIES and index column to years
        categories = list(hist['dimension']['Tiedot']['category']['label'].values())
        years = list(hist['dimension']['Vuosi']['category']['label'].keys())
        values = hist['value']

        values = np.array(values)
        values = np.reshape(values,(-1,n_years))

        data = {}
        data['Year'] = years

        i = 0
        for cat in categories:
            data[cat] = values[i,:]
            i += 1
        
        data = pd.DataFrame(data)
        data.set_index('Year', inplace=True)
        return data

    def get_historical_options(self):
        """
        Returns a dict containing the possible categories and timerange that the user can choose to view data from.
        Dict is structured followingly:
        
        {
            'categories':{
                <category_name>: <category_id>
            },
            'timerange': [a list of available years]
        }

        """
        return self.hist_options

    def get_realtime_options(self):
        """
        Returns a dict containing all possible values for each station, table, tablevariable etc.
        Formatted:
        {
            <station name>:
            {
                'id': <station_id>,
                'tables': 
                {
                    <tablename>:
                    {
                        'id': <table_id>
                        'variables':
                        {
                            'variable': 'id'
                        }
                    }
                }

            }
        }
        
        The keys in these dicts can be used as dropdown menu options to be displayed in the UI

        """
        return self.realtime_options

