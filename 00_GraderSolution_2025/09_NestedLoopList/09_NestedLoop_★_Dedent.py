output = []

for i in range(0, int(input())):
    line = input()

    whiteSpaceCounter = 0
    for e in line:
        if e == ".": whiteSpaceCounter += 1
        else: break

    whiteSpaceCounter /= 2
    line = line[int(whiteSpaceCounter)::]

    output.append(line)

for e in output: print(e)
