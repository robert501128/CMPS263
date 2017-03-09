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
	dataObj['electrical power'] = row[2].encode("ascii")
	dataObj['transportation'] = row[5].encode("ascii")
	data.append(dataObj)

res = {}
for i in range(0, len(countries)):
	res[countries[i]] = data[i]
print res

