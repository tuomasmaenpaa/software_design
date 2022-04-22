import requests
import json
from pathlib import Path
import pandas as pd
import numpy as np
from io import StringIO



class DataFetcher:
    def __init__(self):
        pass
    
    def get_historical(self, years = [], categories = ["Khk_yht", "Khk_yht_index", "Khk_yht_las", "Khk_yht_las_index"]):
        """
        Returns a Pandas dataframe of STATFI data
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

        if res.status_code != 200:
            return pd.DataFrame()

        return self.__hist_to_dataframe(json.loads(res.text))

    def get_realtime(self, start_date, end_date, table_variables, interval, aggregation):
        """
        Returns a Pandas dataframe from SMEAR based on the parameters
        """

        url = 'https://smear-backend.rahtiapp.fi/search/timeseries/csv?'
        url += 'aggregation=' + aggregation
        url += '&interval=' + str(interval)
        url += '&from=' + start_date
        url += '&to=' + end_date

        for t_v in table_variables:
            url += '&tablevariable=' + t_v
        res = requests.get(url)

        # If request was faulty, return empty dataframe
        if res.status_code != 200:
            return pd.DataFrame()

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
    
   
    
    def __hist_to_dataframe(self, hist):
        """
        Converts historical data from JSON-format to Pandas dataframe
        """


        n_years = hist['size'][1]
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
