from DataFetcher import DataFetcher
import json
from textwrap import indent
import pandas as pd
import numpy as np
import requests

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


"""
print()
print("==============================================================")
print()


aggregation = 'NONE'
start_date = '2022-03-24T11:00:00.000'
end_date = '2022-03-24T12:00:00.000'
interval = 1
table_variables = ['VAR_META.SO2_1', 'HYY_META.SO2168', 'KUM_META.SO_2']

realtime = d.get_realtime(start_date, end_date, table_variables, interval, aggregation)
print(realtime.head())
#print(json.dumps(realtime, indent=4))

##print(json.dumps(d.get_historical_options(), indent=4))

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
    print(json.dumps(realtime_options[i], indent=4))
    break

keywords = ['CO\u2082', 'NO\u2093', 'NO', 'SO\u2082',  'CO', 'SO']
def get_variable_titles(station_id, table_id, variable_id):
    url = 'https://smear-backend.rahtiapp.fi/station/' + station_id + '/table/' + table_id + '/variable/' + variable_id 
    res = requests.get(url)
    p = json.loads(res.text)
    #print(json.dumps(p, indent=4))
    try:
        if any(map(p['title'].__contains__, keywords)):
            print(p['title'])
            return True, p['title']
        return False, ''
    except:
        return False, ''

# Lets find out where CO2, SO2 and NO are hidden for our stations

"""
{
    <station_name>:
    {
        'id': <station_id>
        'variables':
        {
            <Gas name>: <table.variable>
        }
    }

}

"""

def form_tablevariable(table, variable):
    return '.'.join([table,variable])

menu_options = {}

for station in s:
    menu_options[station] = {}
    station_id = realtime_options[station]['id']
    menu_options[station]['id'] = realtime_options[station]['id']
    menu_options[station]['variables'] = {}

    for table in realtime_options[station]['tables']:
       
        table_id = realtime_options[station]['tables'][table]['table_id']
        
        for variable in realtime_options[station]['tables'][table]['variables']:
           
            variable_id = realtime_options[station]['tables'][table]['variables'][variable]
            relevant, title = get_variable_titles(station_id, table_id, variable_id)
            
            if relevant:
                menu_options[station]['variables'][title] = form_tablevariable(table, variable)


print(json.dumps(menu_options, indent=4))


with open('menu.json', 'w') as outfile:
    json.dump(menu_options, outfile)