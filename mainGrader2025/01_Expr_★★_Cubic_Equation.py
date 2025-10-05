coefficient = input().split()
a = float(coefficient[0])
b = float(coefficient[1])
c = float(coefficient[2])
d = float(coefficient[3])

A = -(b/(3*a))
B = -(1/(3*a))*(1/2*(2*b**3-9*a*b*c+27*a**2*d+((2*b**3-9*a*b*c+27*a**2*d)**2-4*(b**2-3*a*c)**3)**(1/2)))**(1/3)
C = -(1/(3*a))*(1/2*(2*b**3-9*a*b*c+27*a**2*d-((2*b**3-9*a*b*c+27*a**2*d)**2-4*(b**2-3*a*c)**3)**(1/2)))**(1/3)

x = A+B+C
print(round(x, 3))
