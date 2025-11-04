winningSet, losingSet = set([]), set([])

for i in range(0, int(input())):
    winner, loser = input().split()

    winningSet.add(winner)
    losingSet.add(loser)

print(sorted(list(winningSet-losingSet)))
