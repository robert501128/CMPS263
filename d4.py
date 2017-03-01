import urllib2
import requests
import pprint
from bs4 import BeautifulSoup

page = urllib2.urlopen('https://en.wikipedia.org/wiki/Government_incentives_for_plug-in_electric_vehicles').read()
soup = BeautifulSoup(page,'lxml')
#print(soup.prettify())
data = []
table = soup.find('table', {'class': 'wikitable'})
#pprint.pprint(table)
#table_body = table.find('tbody')
#pprint.pprint(table_body)
#rows = table_body.find_all('tr')
rows = table.findAll(lambda tag: tag.name=='tr')
#pprint.pprint(rows)
for row in rows:
	cols = row.find_all('td')
	cols = [ele.text.strip() for ele in cols]
	data.append([ele for ele in cols if ele]) 
pprint.pprint(data)