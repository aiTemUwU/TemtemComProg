data = []

for i in range(0 ,int(input())):
    x, y = (float(i) for i in input().split())
    distant = (x**2+y**2)**(1/2)
    data.append([distant, i+1, x, y])
    
data.sort()

print(f"#{data[2][1]}: ({data[2][2]}, {data[2][3]})")
