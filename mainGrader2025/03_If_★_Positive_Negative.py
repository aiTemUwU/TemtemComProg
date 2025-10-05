num = int(input())
posNeg = ""
evenOdd = ""

if num > 0: posNeg = "positive"
elif num == 0: posNeg = "zero"
else: posNeg = "negative"

evenOdd = "even" if num%2 == 0 else "odd"

print(f"{posNeg}\n{evenOdd}")