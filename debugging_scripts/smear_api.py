"""
This file contains functions that can be utilized in Datafetcher 
This file is NOT going to be used in the final product
"""

from textwrap import indent
import requests
import json


def get_smear_stations():
    """
    Returns a list of tuples (station, id) of all available SMEAR API stations
    """
    res = requests.get('https://smear-backend.rahtiapp.fi/search/station')
    p = json.loads(res.text)
    #print(json.dumps(p, indent=4))

    stations = [(p[i]['name'], str(p[i]['id'])) for i in range(len(p)) ]
    return stations

def get_smear_station_tables(station_id):
    """
    Returns a list of tuples (name, id) of variable tables for station id
    """
    url = 'https://smear-backend.rahtiapp.fi/station/' + station_id + '/table'
    res = requests.get(url)
    p = json.loads(res.text)

    tables = [(p[i]['name'], str(p[i]['id'])) for i in range(len(p)) ]

    return tables

def get_smear_station_table_variables(station_id, table_id):

    """
    Returns a list of tuples (name, id) of variable tables for station id
    """
    url = 'https://smear-backend.rahtiapp.fi/station/' + station_id + '/table/' + table_id + '/variable'
    res = requests.get(url)
    p = json.loads(res.text)

    variables = [(p[i]['name'], str(p[i]['id'])) for i in range(len(p)) ]

    return variables

def get_smear_timeseries(start_date, end_date, table_variables, interval = 60, aggregation='NONE'):
    """
    Fetches timeseries data for selected stations, for set timeframe, according to set interval (default 60min)
    and for set aggregation (default NONE).

    TODO: table_variables contains ??? ready strings format <VAR.TABLE> or strings VAR and TABLE separately

            THIS VERSION ASSUMES READY STRINGS
    
    """
    
    url = 'https://smear-backend.rahtiapp.fi/search/timeseries?'
    url += 'aggregation=' + aggregation
    url += '&interval=' + str(interval)
    url += '&from=' + start_date
    url += '&to=' + end_date

    for t_v in table_variables:
        url += '&tablevariable=' + t_v
    
    print(url)
    res = requests.get(url)
    return res


stations = get_smear_stations()
tables = get_smear_station_tables(stations[0][1])
variables = get_smear_station_table_variables(stations[0][1], tables[0][1])

#print(tables[0])
#print(variables)


# Fetch example JSON to use as dummy data for developing other parts while datafetcher isn't ready

aggregation = 'NONE'
start_date = '2022-01-20T01:00:00.000'
end_date = '2022-01-20T02:00:00.000'
interval = 1
table_variables = ['VAR_META.SO2_1', 'HYY_META.SO2168', 'KUM_META.SO_2']

dummy = get_smear_timeseries(start_date, end_date, table_variables, interval, aggregation)

data = json.loads(dummy.text)
dummy = json.dumps(data)
with open('dummy.json', 'w') as outfile:
    outfile.write(dummy)

