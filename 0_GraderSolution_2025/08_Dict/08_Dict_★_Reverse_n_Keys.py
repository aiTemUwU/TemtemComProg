def reverse(d):
	newDict = {}
	
	for key in d.keys():
		newDict.update({d.get(key):key})
		
	return newDict

def keys(d, v):
	outPut = []
	
	for key in d.keys():
		if d.get(key) == v:
			outPut.append(key)
		else: pass
	
	return outPut

exec(input().strip())