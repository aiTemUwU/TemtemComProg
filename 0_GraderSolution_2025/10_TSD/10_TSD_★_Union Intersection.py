unionSet, intersectSet = set([]), set([])

n = int(input())

if n != 0:
    nums = input().split()
    for e in nums:
        unionSet.add(e)
        intersectSet.add(e)

    for i in range(0, n-1):
        nums = set(input().split())

        unionSet = unionSet.union(nums)
        intersectSet = intersectSet.intersection(nums)
else: pass

print(len(unionSet))
print(len(intersectSet))
