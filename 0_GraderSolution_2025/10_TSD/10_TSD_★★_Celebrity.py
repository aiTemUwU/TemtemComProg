def knows(R, x, y):
    if y in R.get(x): return True
    else: return False

def is_celeb(R, x):
    if R.get(x) != set([]) and R.get(x) != set([x]): return False

    for person in set(R.keys())-set([x]):
        if not knows(R, person, x):
            return False

    return True

def find_celeb(R):
    for person in R.keys():
        if is_celeb(R, person): return person
        else: pass
    return None

def read_relations():
    R = dict()
    nameSet = set([])
    while True:
        d = input().split()
        if len(d) == 1: break

        knows, known = d[0], d[1]
        nameSet = nameSet.union(set([knows, known]))
        if knows not in R.keys():
            R.update({knows:set([known])})
        else: R.update({knows:R.get(knows).union(set([known]))})

    for name in nameSet:
        if name not in R.keys(): R.update({name:set([])})
        else: pass

    return R

def main():
    R = read_relations()
    c = find_celeb(R)

    if c == None:
        print("Not Found")
    else: print(c)

exec(input().strip())
