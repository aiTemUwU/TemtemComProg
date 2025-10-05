a = float(input())
b = float(input())
c = float(input())

x1 = (-b-((b**2-4*a*c)**(1/2)))/(2*a)
x2 = (-b+((b**2-4*a*c)**(1/2)))/(2*a)

print(f"{round(x1, 3)} {round(x2, 3)}")