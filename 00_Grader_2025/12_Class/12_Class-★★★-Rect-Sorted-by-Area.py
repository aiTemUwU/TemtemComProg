class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x},{self.y})"

class Rect:
    def __init__(self, p1, p2):
        self.lowerleft = p1
        self.upperright = p2
    def __str__(self):
        return f"{self.lowerleft}-{self.upperright}"
    
    def area(self):
        p1x = self.lowerleft.x
        p1y = self.lowerleft.y

        p2x = self.upperright.x
        p2y = self.upperright.y

        return (p2x-p1x) * (p2y-p1y)
    
    def __lt__(self, rhs):
        return self.area() < rhs.area()


n = int(input())
rects = []
for i in range(n):
    x1, y1, x2, y2 = [int(e) for e in input().split()]
    rects.append(Rect(Point(x1, y1), Point(x2, y2)))
rects.sort()
for i in range(n):
    print(rects[i])