def distance1(x1, y1, x2, y2):
	d = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
	return d

def distance2(p1, p2):
	x1, y1 = p1[0], p1[1]
	x2, y2 = p2[0], p2[1]

	return distance1(x1, y1, x2, y2)

def distance3(c1, c2):
	x1, y1, r1 = c1[0], c1[1], c1[2]
	x2, y2, r2 = c2[0], c2[1], c2[2]
	d3 = distance1(x1, y1, x2, y2)

	if r1 + r2 >= d3:
		overlap = True
	else: overlap = False

	return d3, overlap

def perimeter(points):
	perimeter = 0
	for i in range(0, len(points)):
		x1, y1 = points[i-1][0], points[i-1][1]
		x2, y2 = points[i][0], points[i][1]

		perimeter += distance1(x1, y1, x2, y2)

	return perimeter

exec(input().strip())
