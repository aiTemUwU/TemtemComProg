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

        delVal, delIndex = [], []
            
        commonCase = ["I", "V", "X", "L", "C", "D", "M"][::-1]
        commonValue = [1, 5, 10, 50, 100, 500, 1000][::-1]

        specialCase = ["IV", "IX", "XL", "XC", "CD", "CM"][::-1]
        specialUnfinisedCase = [["I", "I", "I", "I"], ["V", "I", "I", "I", "I"], ["V", "V", "V", "V"], ["X", "V", "V", "V", "V"], ["L", "L", "L", "L"], ["C", "L", "L", "L", "L"]][::-1]

        for i in range(0, len(commonCase)):
            if currentVal >= commonValue[i]:
                countedLetterRep = currentVal//commonValue[i]

                currentVal -= countedLetterRep * commonValue[i]
                for j in range(0, countedLetterRep):
                    outputRoman.append(commonCase[i])
            else: pass
            
        for i in range(2, len(outputRoman)):
            checkingLetters = outputRoman[i-2:i+1]
            if checkingLetters in [["I", "I", "I"], ["V", "V", "V"], ["L", "L", "L"]]:
                if outputRoman[i-4:i+1] in specialUnfinisedCase:
                    delVal.append(specialCase[specialUnfinisedCase.index(outputRoman[i-4:i+1])])
                    delIndex.append([i-4, i+1])
                elif outputRoman[i-3:i+1] in specialUnfinisedCase:
                    delVal.append(specialCase[specialUnfinisedCase.index(outputRoman[i-3:i+1])])
                    delIndex.append([i-3, i+1])
                else: pass

        delVal = delVal[::-1]
        delIndex = delIndex[::-1]

        for i in range(0, len(delIndex)):
            del outputRoman[delIndex[i][0]:delIndex[i][1]]
            outputRoman.insert(delIndex[i][0], delVal[i])
            
        outputRomanStr = "".join(letter for letter in outputRoman)

        return roman(outputRomanStr)

t, r1, r2 = input().split()
a = roman(r1); b = roman(r2)
if t == "1": print(a < b)
elif t == "2": print(int(a), int(b))
elif t == "3": print(str(a), str(b))
elif t == "4": print(int(a + b))
else: print(str(a + b))