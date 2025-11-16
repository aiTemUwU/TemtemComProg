class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def __str__(self):
        return f"({self.value} {self.suit})"
    
    def next1(self):
        selfIndex = deck.index([self.value, self.suit]) + 1
        return Card(deck[selfIndex][0], deck[selfIndex][1])

    def next2(self):
        self.value = self.next1().value
        self.suit = self.next1().suit
        return
        
deck = []
suitList = ["club", "diamond", "heart", "spade"]
scoreList = ["3", "4", "5", "6", "7", "8", "9", "J", "Q", "K", "A", "2"]

for score in scoreList:
    for suit in suitList:
        deck.append([score, suit])
deck *= 2

n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])