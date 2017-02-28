import pandas as pd


d1 = pd.read_csv('data/1_vehicles.csv', low_memory=False)
d2 = pd.read_csv('data/3_alt_fuel_stations.csv', low_memory=False)
d3 = pd.read_csv('data/5_roadster-survey-reports.csv', sep='\t')