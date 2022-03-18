import requests
import json
from pathlib import Path

class DataFetcher():
    def __init__(self):
        self.hist_options = self._init_hist_options()
        self.realtime_options = self._init_realtime_options()
    
    """ TODO
            
            data could be returned as JSON, format following
            That would make data handling easier and uniform in model

            {
                data: [[data arrays]],
                labels: [labels],
                title: 'title'
            }
            
            Not sure if title is necessary
    """

    def _init_hist_options(self):
        """
        Private function to be used in finding the historical data limits
        """
        limits = self._get_historical_limits()

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

    def _init_realtime_options(self):
        options = {}

        stations = self._get_stations()


        for station, station_id in stations:

            options[station] = {'id': station_id}
            options[station]['tables'] = {}
            tables = self._get_smear_station_tables(station_id)

            for table, table_id in tables:

                options[station]['tables'][table] = {'table_id': table_id}
                options[station]['tables'][table]['variables'] = {}
                
                variables = self._get_smear_station_table_variables(station_id, table_id)

                for variable, variable_id in variables:

                    options[station]['tables'][table]['variables'][variable] = variable_id

        return options

    def get_historical(self, years = [], categories = ["Khk_yht", "Khk_yht_index", "Khk_yht_las", "Khk_yht_las_index"]):
        """
        Returns a JSON of data from STATFI based on given parameters
        """
        path = Path(__file__).parent / "request.json"

        url = 'https://pxnet2.stat.fi/PXWeb/api/v1/en/ymp/taulukot/Kokodata.px'
        payload = open(path)
        payload = json.load(payload)

        payload['query'][0]['selection']['values'] = categories
        payload['query'][1]['selection']['values'] = years

        payload = json.dumps(payload)

        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        res = requests.post(url, data=payload, headers=headers)

        return json.loads(res.text)

    def get_realtime(self, start_date, end_date, table_variables, interval, aggregation):
        """
        Returns a JSON of data from SMEAR based on the parameters
        """

        url = 'https://smear-backend.rahtiapp.fi/search/timeseries?'
        url += 'aggregation=' + aggregation
        url += '&interval=' + str(interval)
        url += '&from=' + start_date
        url += '&to=' + end_date

        for t_v in table_variables:
            url += '&tablevariable=' + t_v
        res = requests.get(url)

        return json.loads(res.text)
    
    def _get_stations(self):
        """
        Returns a list of tuples (station, id) of all available SMEAR API stations
        """
        res = requests.get('https://smear-backend.rahtiapp.fi/search/station')
        p = json.loads(res.text)

        stations = [(p[i]['name'], str(p[i]['id'])) for i in range(len(p)) ]
        return stations

    def _get_smear_station_tables(self, station_id):
        """
        Returns a list of tuples (name, id) of variable tables for station id
        """
        url = 'https://smear-backend.rahtiapp.fi/station/' + station_id + '/table'
        res = requests.get(url)
        p = json.loads(res.text)

        tables = [(p[i]['name'], str(p[i]['id'])) for i in range(len(p)) ]

        return tables   

    def _get_smear_station_table_variables(self, station_id, table_id):

        """
        Returns a list of tuples (name, id) of variable tables for station id
        """
        url = 'https://smear-backend.rahtiapp.fi/station/' + station_id + '/table/' + table_id + '/variable'
        res = requests.get(url)
        p = json.loads(res.text)

        variables = [(p[i]['name'], str(p[i]['id'])) for i in range(len(p)) ]

        return variables
 
    def _get_historical_limits(self):
        """
        Get the years and categories from which historical data can be used
        """
        res = requests.get('https://pxnet2.stat.fi/PXWeb/api/v1/en/ymp/taulukot/Kokodata.px')
        return json.loads(res.text)
 
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

