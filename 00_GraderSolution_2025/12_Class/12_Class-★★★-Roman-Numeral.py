class roman:
    def __init__(self, r):
        self.r = r


    def __lt__(self, rhs):
        return int(self) < int(rhs)


    def __str__(self):
        return self.r


    def __int__(self):
        delList, rList, totVal = [], [], 0
        for e in self.r: rList.append(e)

        specialCase = ["IV", "IX", "XL", "XC", "CD", "CM"]
        specialValue = [4, 9, 40, 90, 400, 900]

        commonCase = ["I", "V", "X", "L", "C", "D", "M"]
        commonValue = [1, 5, 10, 50, 100, 500, 1000]

        for i in range(1, len(self.r)):
            if self.r[i-1] + self.r[i] in specialCase:
                totVal += specialValue[specialCase.index(self.r[i-1] + self.r[i])]
                delList += [i-1, i]
        
        delList = sorted(delList)[::-1]
        for index in delList: poppedElement = rList.pop(index)

        for letter in rList: totVal += commonValue[commonCase.index(letter)]

        return totVal


    def __add__(self, rhs):
        return roman.intToRoman(int(self) + int(rhs))
    

    @staticmethod
    def intToRoman(value):
        outputRoman = []
        currentVal = int(value)

        syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        for i in range(0, len(syms)):
            if currentVal >= vals[i]:
                countedLetter = currentVal//vals[i]
                for j in range(0, countedLetter): outputRoman.append(syms[i])
                currentVal -= countedLetter * vals[i]
            if currentVal == 0: break

        return roman("".join(letter for letter in outputRoman))

t, r1, r2 = input().split()
a = roman(r1); b = roman(r2)
if t == "1": print(a < b)
elif t == "2": print(int(a), int(b))
elif t == "3": print(str(a), str(b))
elif t == "4": print(int(a + b))
else: print(str(a + b))

