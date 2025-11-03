def first_fit(L, e):
    isPossibleFit = False

    for subList in L:
        if sum(subList) + e > 100: pass
        else:
            isPossibleFit = True
            break

    if not isPossibleFit:
        L.append([e])
    else:
        for subList in L:
            if sum(subList) + e <= 100:
                subList.append(e)
                break
            else: pass

    return


def best_fit(L, e):
    sumDict, sumList = {}, []
    isPossibleFit = False

    for subList in L:
        if sum(subList) + e > 100: pass
        else:
            isPossibleFit = True
            break

    if not isPossibleFit:
        L.append([e])
    else:
        for subList in L:
            if sum(subList) + e > 100: pass
            else: sumDict.update({abs(sum(subList)+e-100):subList})

        bestFitKey = min(sumDict.keys())
        bestFitList = sumDict.get(bestFitKey)

        for subList in L:
            if subList == bestFitList:
                subList.append(e)
                break
            else: pass

    return


def partition_FF(D):
    partitionedList = [[]]
    for e in D: first_fit(partitionedList, e)

    return partitionedList


def partition_BF(D):
    partitionedList = [[]]
    for e in D: best_fit(partitionedList, e)

    return partitionedList


exec(input().strip())
