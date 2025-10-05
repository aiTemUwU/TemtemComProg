def total(pocket):
	totCash = 0
	for e in pocket.keys():
		totCash += pocket.get(e)*e
	
	return totCash

def take(pocket, money):
	for e in money.keys():
		if e in pocket.keys():
			pocket.update({e:pocket.get(e)+money.get(e)})
		else: pocket.update({e:money.get(e)})
	return

def pay(pocket, amt):
	
	if amt > total(pocket): return {}
	else: pass
	
	paidDict = {}
	for value in sorted(pocket.keys(), reverse = True):
		
		if amt >= value:
			paidN = min(pocket.get(value), amt // value)
			
			paidDict.update({value:paidN})
			pocket.update({value:pocket.get(value)-paidN})
			amt -= value * paidN
		else: pass
		
	if amt != 0:
		take(pocket, paidDict)
		return {}
	else: return paidDict

exec(input().strip())