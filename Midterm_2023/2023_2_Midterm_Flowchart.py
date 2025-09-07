n, a, b = [int(e) for e in input().split()]

if a > b:
	d, e = -1, -1
	while n < a:
		c = int(input())
		if c > d:
			d, e = c, d
		else:
			if c > e:
				e = c
			else:
				pass
		n += b
else:
	c, d, e, f = [int(input()) for i in range(0, 4)]
	if e < f:
		e, f = f, e
	else:
		pass
	if d < e:
		d, e = e, d
	else:
		pass
	if c < d:
		c, d = d, c
	else:
		pass
	if d > e:
		if d > f:
			pass
		else:
			d, f = f, d
	else:
		if e > f:
			d, e = e, d
		else:
			d, f = f, d

print(d, e)

#test case 2 problem