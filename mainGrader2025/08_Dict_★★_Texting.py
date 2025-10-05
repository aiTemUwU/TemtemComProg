text2keysDict = {" " : "0", "abc" : "2", "def" : "3", "ghi" : "4", "jkl" : "5", "mno" : "6", "pqrs" : "7", "tuv" : "8", "wxyz" : "9"}

def reverse(dict):
	reversedDict = {}
	
	for e in dict.keys():
		reversedDict.update({dict.get(e) : e})
		
	return reversedDict

keys2textDict = reverse(text2keysDict)


def keys2text(keys):
	keys = keys.split()
	outPut = ""
	
	for i in range(0, len(keys)):
		text = keys2textDict.get(keys[i][0])[len(keys[i])-1]
		outPut += text
		
	return outPut

def text2keys(text):
	filteredText = ""
	outPut = ""
	
	for e in text:
		if e == " ": filteredText += e
		if not e.isalpha(): pass
		else: filteredText += e
	
	filteredText = filteredText.lower()
	
	for e in filteredText:
		for r in text2keysDict.keys():
			if e in r:
				outPut += text2keysDict.get(r)*(r.index(e)+1) + " "
			else: pass
	
	return outPut[0:-1]

exec(input().strip())