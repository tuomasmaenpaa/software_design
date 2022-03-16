from DataFetcher import DataFetcher
import json
from textwrap import indent

d = DataFetcher()
historical = d.get_historical([2011, 2012, 2013])
print(json.dumps(historical, indent=4))

print()
print("==============================================================")
print()


aggregation = 'NONE'
start_date = '2022-01-20T01:00:00.000'
end_date = '2022-01-20T02:00:00.000'
interval = 1
table_variables = ['VAR_META.SO2_1', 'HYY_META.SO2168', 'KUM_META.SO_2']

realtime = d.get_realtime(start_date, end_date, table_variables, interval, aggregation)

print(json.dumps(realtime, indent=4))