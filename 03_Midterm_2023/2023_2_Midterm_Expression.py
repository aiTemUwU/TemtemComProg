a, b, c1, c2, c3 = [float(input()) for i in range(0, 5)]
barWidth = (b - a)/10
y, area = 0, 0

for i in range(0, 10):
	x = a + barWidth*i
	y = c1*(x**2) + c2*x + c3
	
	area += y * barWidth
	
print(round(area, 2))
