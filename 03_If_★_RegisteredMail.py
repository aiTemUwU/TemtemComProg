weight = float(input())
cost = "Reject"

if weight <= 100: cost = 18
elif weight <= 250: cost = 22
elif weight <= 500: cost = 28
elif weight <= 1000: cost = 38
elif weight <= 2000: cost = 58
else: pass

print(cost)