import math
numbers = [float(i) for i in input().split()]

if len(numbers) != 2:
	print("Error!")
else:
	v, theta = numbers[0], math.radians(numbers[1])
	
	hmax = ((v**2)*(math.sin(theta))**2)/(2*9.81)
	R = ((v**2)*math.sin(2*theta))/9.81
	T = abs((2*v*math.sin(theta))/9.81)
	
	print(f"{round(hmax, 2):.2f} {round(R, 2):.2f} {round(T, 2):.2f}")
