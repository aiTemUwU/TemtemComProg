def make_int_list(x):
	return [int(i) for i in x.split()]

def is_odd(e):
	if e % 2 == 0: return False
	else: return True

def odd_list(alist):
	oddList = []
	for i in range(0, len(alist)):
		if is_odd(alist[i]):
			oddList.append(alist[i])
		else: pass
	
	return oddList

def sum_square(alist):
	sumVal = 0
	for i in range(0, len(alist)):
		sumVal += alist[i]**2
		
	return sumVal

exec(input().strip())