import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
import gzip
import math as m

stations_arg = sys.argv[1]
cities_arg = sys.argv[2]
output_arg = sys.argv[3]

station_fh = gzip.open(stations_arg, 'rt', encoding='utf-8')
stations_df = pd.read_json(station_fh, lines=True)
cities_df = pd.read_csv(cities_arg)

stations_df['avg_tmax'] = stations_df['avg_tmax'] / 10 

cities_df = cities_df[np.isfinite(cities_df.population)]
cities_df = cities_df[np.isfinite(cities_df.area)].reset_index(drop=True) 
cities_df['area'] = cities_df['area'] / 1000000 

cities_df = cities_df[cities_df.area <= 10000] 

cities_df.reset_index(drop=True)

cities_df['density'] = cities_df['population'] / cities_df['area'] 

def distance(city, stations):
    p = float(m.pi/180)
    city_lat = city['latitude']
    city_long = city['longitude']

    d = 0.5 - np.cos((stations['latitude']-city_lat)*p)/2 + np.cos(city_lat*p) * np.cos(stations['latitude']*p) * (1- np.cos((stations['longitude']-city_long)*p))/2
    
    return 12742*np.arcsin(np.sqrt(d))

def best_tmax(city, stations): 
    stations['distance'] = distance(city, stations)
    station = stations_df[stations_df['distance'] == stations_df['distance'].min()]
    
    station = station.reset_index(drop=True)
    
    return station.loc[0, 'avg_tmax']

cities_df['avg_tmax'] = cities_df.apply(best_tmax, axis=1, stations=stations_df)

plt.title('Temperature vs Population Density')
plt.ylabel('Population Density (people/km\u00b2)')
plt.xlabel('Avg Max Temperature (\u00b0C)')
plt.scatter(cities_df['avg_tmax'], cities_df['population'])

plt.savefig(output_arg)