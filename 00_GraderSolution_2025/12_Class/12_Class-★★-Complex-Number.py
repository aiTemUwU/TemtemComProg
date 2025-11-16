class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        a, b = self.a, self.b

        if a == 0:
            if b == 0: return "0"
            elif b == 1: return f"i"
            elif b == -1: return f"-i"
            else: return f"{b}i"
        else:
            if b == 0: return f"{a}"
            if b == 1: return f"{a}+i"
            if b == -1: return f"{a}-i"
            elif b > 0: return f"{a}+{b}i"
            elif b < 0: return f"{a}-{-b}i"
    
    def __add__(self, rhs):
        a, b = self.a, self.b
        c, d = rhs.a, rhs.b

        sum = Complex(a+c, b+d)
        return str(sum)
    
    def __mul__(self, rhs):
        a, b = self.a, self.b
        c, d = rhs.a, rhs.b

        mult = Complex(a*c - b*d, a*d + b*c)
        return str(mult)
    
    def __truediv__(self, rhs):
        a, b = self.a, self.b
        c, d = rhs.a, rhs.b

        reOutput = (a*c + b*d)/(c**2 + d**2)
        imOutput = (b*c - a*d)/(c**2 + d**2)

        output = Complex(reOutput, imOutput)
        return str(output)

t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a, b)
c2 = Complex(c, d)
if t == 1: print(c1)
elif t == 2: print(c2)
elif t == 3: print(c1+c2)
elif t == 4: print(c1*c2)
else: print(c1/c2)