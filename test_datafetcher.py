from DataFetcher import DataFetcher
import json
from textwrap import indent
import pandas as pd
import numpy as np

d = DataFetcher()

def hist_to_dataframe(hist):
    n_categories = hist['size'][0]
    n_years = hist['size'][1]
    categories = list(hist['dimension']['Tiedot']['category']['label'].keys())
    years = list(hist['dimension']['Vuosi']['category']['label'].keys())
    values = hist['value']
    c = values
    values = np.array(values)
    values = np.reshape(values,(-1,n_years))

    data = {}
    data['Year'] = years

    i = 0
    for cat in categories:
        data[cat] = values[i,:]
        i += 1
    
    data = pd.DataFrame(data)
    return data

historical = d.get_historical([2011, 2012, 2013])
#print(json.dumps(historical, indent=4))

print(historical.head())



print()
print("==============================================================")
print()


aggregation = 'NONE'
start_date = '2022-01-20T01:00:00.000'
end_date = '2022-01-20T02:00:00.000'
interval = 1
table_variables = ['VAR_META.SO2_1', 'HYY_META.SO2168', 'KUM_META.SO_2']

#realtime = d.get_realtime(start_date, end_date, table_variables, interval, aggregation)
#print(realtime.head())
#print(json.dumps(realtime, indent=4))

##print(json.dumps(d.get_historical_options(), indent=4))
"""
structure:

{
    <name>:
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

"""
realtime_options = d.get_realtime_options()
#print(json.dumps(realtime_options, indent=4))
s = list(realtime_options.keys())
print(f"{len(s)} stations in SMEAR:")
for i in s:
    print(" " + i)