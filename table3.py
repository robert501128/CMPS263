from pdftables import get_tables
all_tables = get_tables(open('table3.pdf', 'rb'))
#print all_tables
#headers = ['electrical power','transportation']
rows1 = all_tables[0][5:]
rows2 = all_tables[1][4:]
countries = []
data =[]

for row in rows1 + rows2:
	if row[0].startswith('U.S.'):
		continue;
	if row[0].startswith('Total'):
		break;
	if row[0] == '':
		continue;
	countries.append(row[0].encode("ascii"))
	dataObj = {}
	dataObj['commercial'] = float(row[1].encode("ascii"))*1000000
	dataObj['electrical power'] = float(row[2].encode("ascii"))*1000000
	dataObj['residential'] = float(row[3].encode("ascii"))*1000000
	dataObj['industrial'] = float(row[4].encode("ascii"))*1000000
	dataObj['transportation'] = float(row[5].encode("ascii"))*1000000
	dataObj['total'] = float(row[6].encode("ascii"))*1000000
	data.append(dataObj)

res = {}
for i in range(0, len(countries)):
	res[countries[i]] = data[i]
print res

