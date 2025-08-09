import math

pi = math.pi
e = math.e

n = int(input())

lowerBound = (math.sqrt(2*pi))*(n**(n+1/2))*(e**(-n+(1/(12*n+1))))
upperBound = (math.sqrt(2*pi))*(n**(n+1/2))*(e**(-n+(1/(12*n))))

print(lowerBound)
print(upperBound)