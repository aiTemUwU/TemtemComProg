class piggybank:
    def __init__(self):
        self.coins = {}
        self.coinsCount = 0

    def add(self, v, n):
        v = float(v)
        if self.coinsCount + n > 100:
            return False
        else:
            if v not in self.coins.keys():
                self.coins.update({v:n})
            else: self.coins.update({v:self.coins.get(v)+n})
            
            self.coinsCount += n
            return True
        
    def __float__(self):
        totVal = 0
        for coinType in self.coins.keys():
            totVal += coinType * self.coins.get(coinType)
        return float(totVal)

    def __str__(self):
        sortingList = []
        output = ""
        for coinType in self.coins.keys():
            sortingList.append([coinType, self.coins.get(coinType)])
        sortingList = sorted(sortingList)

        for coinType in sortingList:
            output += f"{coinType[0]}:{coinType[1]}, "

        output = output[:-2]
        output = "{" + output + "}"
        return output

cmd1 = input().split(";")
cmd2 = input().split(";")
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)

"""
p1.add(1.11, 2); print(float(p1), p1)
print(float(p2), p2)

p1.add(0.25, 1); p1.add(5, 1); p1.add(0.25, 2); p1.add(5.0, 1)
print(float(p1), str(p1))

p1.add(0.25, 1); print(p1.add(0.25, 100))
print(p1.add(0.25, 99)); print(float(p1))
"""