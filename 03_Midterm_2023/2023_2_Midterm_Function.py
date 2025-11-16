def contain_only_alphabets(s):
	if s.strip() == "": return False
	else: pass
	
	for e in s:
		if e == " " or e.isalpha(): pass
		else: return False
		
	return True

def contain_only_digits(s):
	filteringText = ""
	
	for e in s:
		if e in [",", "."] or e.isdigit():
			if e.isdigit(): filteringText += e
			else: pass
		else: return False
	
	if filteringText == "": return False
	else: pass
	
	return True

def sort_numbers_inplace(numbers):
	numericList, strList = [], []
	for e in numbers:
		if isinstance(e, str):
			strList.append(e)
		else: numericList.append(e)
	
	numericList = sorted(numericList)
	strList = sorted(strList)
	
	numbers[:] = numericList + strList
	
	return

def categorize(L):
	l1, l2, l3 = [], [], []
	for e in L:
		if isinstance(e, int) or isinstance(e, float): l2.append(e)
		elif contain_only_alphabets(e): l1.append(e)
		elif contain_only_digits(e): l2.append(e)
		else: l3.append(e)
		
	sort_numbers_inplace(l2)
	
	return l1, l2, l3

exec(input().strip())

#D = [1, '12', 0, '9']
#sort_numbers_inplace(D)
#print(D)
