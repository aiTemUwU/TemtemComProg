iceCreamDict, salesDict = {}, {}
salesList, salesPriceList, topSalesProduct = [], [], []
topSalesCounter, revenue = 0, 0
topSalesStr = ""

for i in range(0, int(input())):
	name, price = input().split()
	iceCreamDict.update({name:float(price)})

for i in range(0, int(input())):
	soldName, quant = input().split()
	quant = float(quant)
	
	if soldName not in iceCreamDict.keys():pass
	elif soldName not in salesDict.keys():
		salesDict.update({soldName:quant*iceCreamDict.get(soldName)})
		revenue += quant*iceCreamDict.get(soldName)
	else:
		oldSales = salesDict.get(soldName)
		salesDict.update({soldName:quant*iceCreamDict.get(soldName)+oldSales})
		revenue += quant*iceCreamDict.get(soldName)

for e in salesDict.keys():
	salesList.append([salesDict.get(e), e])
	salesPriceList.append(salesDict.get(e))

salesList = sorted(salesList)
salesPriceList = sorted(salesPriceList)

for i in range(0, len(salesPriceList)):
	if salesPriceList[i] == max(salesPriceList):
		topSalesProduct.append(salesList[i][1])
	else: pass

for i in range(0, len(topSalesProduct)):
	topSalesStr += f"{topSalesProduct[i]}, "
topSalesStr = topSalesStr[:-2]

if revenue != 0:
	print(f"Total ice cream sales: {revenue}")
	print(f"Top sales: {topSalesStr}")
else:
	print(f"No ice cream sales")