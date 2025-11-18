class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"({self.value} {self.suit})"

    def getScore(self):
        value = self.value
        
        if value == "A": value = 1
        elif value in ["J", "Q", "K"]: value = 10
        else: value = int(value)

        return value

    def sum(self, other):
        selfValue = self.getScore()
        otherValue = other.getScore()

        return (selfValue + otherValue)%10

    def __lt__(self, rhs):
        suitList = ["club", "diamond", "heart", "spade"]
        scoreList = ["3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2"]

        if self.value != rhs.value:
            return scoreList.index(self.value) < scoreList.index(rhs.value)
        else:
            return suitList.index(self.suit) < suitList.index(rhs.suit)

n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].getScore())
print("----------")
for i in range(n-1):
    print(Card.sum(cards[i], cards[i+1]))
print("----------")
cards.sort()
for i in range(n):
    print(cards[i]) 