from hashlib import new
from DataFetcher import DataFetcher
import json
from pathlib import Path
from datetime import datetime



def get_stations(options):
    return(list(options.keys()))

def get_gasses_by_station(options, station_name):
    return(list(options[station_name]['variables']))


def main():

    path = Path(__file__).parent / "menu.json"

    with open(path, 'r') as j:
        options = json.load(j)

    for station in get_stations(options):

        print(f"Available gasses for {station}:")

        for gas in get_gasses_by_station(options, station):
            print('     ' + gas)

main()