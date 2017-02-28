import pandas as pd
from bs4 import BeautifulSoup
import urllib2
import re


def to_int(s):
    num = 0
    for ss in s:
        if ss.isdigit():
            num *= 10
            num += int(ss)
    return num


def findD7():
    f = urllib2.urlopen("https://en.wikipedia.org/wiki/Electric_car_use_by_country")
    soup = BeautifulSoup(f.read(), 'html.parser').find_all('table')
    table = list()
    for xx in soup:
        if 'class' in xx.attrs and xx['class'] == ['wikitable']:
            table.append(xx)

    d7_raw = table[1].find_all('tr')
    column = ['Country', '2015 PEV Stock', '2014 PEV Stock', '2013 PEV Stock']
    d7_dict = {c:[] for c in column}
    for d in d7_raw[3:]:
        i = 0
        if len(d.find_all('td')) < 4:
            continue
        for dd in d.find_all('td'):
            if i >= 4:
                break
            if i == 0:
                d7_dict[column[i]].append(re.search('([a-z]|[A-Z])+(\ ([a-z]|[A-Z])+)*', dd.get_text()[1:]).group(0))
            else:
                fin = re.search('[1-9][0-9]*(,[0-9]+)*', dd.get_text())
                if fin:
                    d7_dict[column[i]].append(to_int(fin.group(0)))
                else:
                    d7_dict[column[i]].append(-1)
            i += 1
    return d7_dict

d1 = pd.read_csv('data/1_vehicles.csv', low_memory=False)
d3 = pd.read_csv('data/3_alt_fuel_stations.csv', low_memory=False)
d5 = pd.read_csv('data/5_roadster-survey-reports.csv', sep='\t')
d7 = pd.DataFrame(data=findD7())

pd.to_pickle(d1, 'd1.pkl')
pd.to_pickle(d3, 'd3.pkl')
pd.to_pickle(d5, 'd5.pkl')
pd.to_pickle(d7, 'd7.pkl')




