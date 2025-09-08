import math
m, n = [int(i) for i in input().split()]

if m < n:
	a, b, c = [int(i) for i in input().split()]
	if m % 2 == 1:
		u, v, w, k = 0, 0, 0, 0
		while not m <= k:
			if a > b:
				if a + c >= k:
					u += 3
					v -= 2
					w += 1
				else:
					u -= 1
					v += 2
					w += 3
			else:
				b = (a+b)/2
			k += 1
		print(u, v, w)
	else:
		a, b = b, a
		a = c - 2*b
		c = a**2
		b = 3*c + 1
		
		print(a, b, c)
else:
	if m == n:
		s = int(input())
		i = s
		k = s
		
		for j in range(0, m-1):
			x = int(input())
			if x < i:
				i = x
			if x > k:
				k = x
		
		print(i*k)
	else:
		if (m+n) % 3 == 0:
			r = m**(1/2) + n**(1/3)
		else:
			r = math.sin((m*math.pi)/(m+n)) + math.cos((n*math.pi)/(m+n))
		print(round(r, 2))