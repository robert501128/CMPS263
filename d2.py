import urllib2
import requests
import pprint
from bs4 import BeautifulSoup

page = urllib2.urlopen('http://www.eia.gov/electricity/state/').read()
soup = BeautifulSoup(page,'lxml')
#print(soup.prettify())
data = []
table = soup.find(lambda tag:tag.name == 'table')
table_body = table.find('tbody')
rows = table_body.find_all('tr')
for row in rows:
	cols = row.find_all('td')
	cols = [ele.text.strip() for ele in cols]
	data.append([ele for ele in cols if ele]) 
pprint.pprint(data) 