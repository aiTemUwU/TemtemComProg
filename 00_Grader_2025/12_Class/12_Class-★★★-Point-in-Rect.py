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
    
    def area(self):
        p1x = self.lowerleft.x
        p1y = self.lowerleft.y
        
        p2x = self.upperright.x
        p2y = self.upperright.y

        return (p2x-p1x) * (p2y-p1y)

    def contains(self, p):
        p1x = self.lowerleft.x
        p1y = self.lowerleft.y

        p2x = self.upperright.x
        p2y = self.upperright.y

        px = p.x
        py = p.y

        if p.x <= p2x and p1x <= p.x and p.y <= p2y and p1y <= p.y: return True
        else: return False

x1, y1, x2, y2 = [int(e) for e in input().split()]
lowerleft = Point(x1, y1)
upperright = Point(x2, y2)
rect = Rect(lowerleft, upperright)
print(rect.area())
m = int(input())
for i in range(m):
    x, y = [int(e) for e in input().split()]
    p = Point(x, y)
    print(rect.contains(p))