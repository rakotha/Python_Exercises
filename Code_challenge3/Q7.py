# Question 7
stock_market = {'AXIS BANK': 7,
    'BHARTI AIRTEL': 5,
    'COAL INDIA': 10,
    'ITC': 1,
    'TCS': 3,
    'L&T': 2,
    'RELIANCE': 9,
    'KOTAK BANK': 8,
    'AMERICAN EXPRESS': 11}

stock_List = sorted(stock_market.items(), key=lambda x:x[1])
print(stock_List[0])
print(stock_List[len(stock_List)-1])
print(stock_List)