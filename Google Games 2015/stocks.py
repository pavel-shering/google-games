stocks = []

with open ("stocks", "r") as f:
	lines = f.readlines()
	for line in lines:
		stocks.append(line)

numpad = { 	'A':2, 'B':2, 'C':2, 
			'D':3, 'E':3, 'F':3,
			'G':4, 'H':4, 'I':4,
			'J':5, 'K':5, 'L':5,
			'M':6, 'N':6, 'O':6,
			'P':7, 'Q':7, 'R':7, 'S':7,
			'T':8, 'U':8, 'V':8,
			'W':9, 'X':9, 'Y':9, 'Z':9 	}

uniquely = {}
l = []

for stock in stocks: 
	x = ""
	for letter in stock.strip():
		x += str(numpad[letter])
	if x in uniquely:
		uniquely[x] += 1 
	else:
		uniquely[x] = 1

l = uniquely.values()
total_unique = 0

for stock in uniquely:
	if uniquely[stock] == 1:
		total_unique += 1	

print total_unique 



		
