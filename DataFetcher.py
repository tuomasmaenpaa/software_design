import requests
import json
from pathlib import Path

class DataFetcher():
    def __init__(self) -> None:
        pass

    
    def get_historical(self ,years = [], categories = ["Khk_yht", "Khk_yht_index", "Khk_yht_las", "Khk_yht_las_index"]):
       
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

        url = 'https://smear-backend.rahtiapp.fi/search/timeseries?'
        url += 'aggregation=' + aggregation
        url += '&interval=' + str(interval)
        url += '&from=' + start_date
        url += '&to=' + end_date

        for t_v in table_variables:
            url += '&tablevariable=' + t_v
        res = requests.get(url)

        return json.loads(res.text)
    
    def get_stations(self):
        """
        Returns a list of tuples (station, id) of all available SMEAR API stations
        """
        res = requests.get('https://smear-backend.rahtiapp.fi/search/station')
        p = json.loads(res.text)

        stations = [(p[i]['name'], str(p[i]['id'])) for i in range(len(p)) ]
        return stations

    def get_smear_station_table_variables(self, station_id, table_id):

        """
        Returns a list of tuples (name, id) of variable tables for station id
        """
        url = 'https://smear-backend.rahtiapp.fi/station/' + station_id + '/table/' + table_id + '/variable'
        res = requests.get(url)
        p = json.loads(res.text)

        variables = [(p[i]['name'], str(p[i]['id'])) for i in range(len(p)) ]

        return variables
 

    
 
    

