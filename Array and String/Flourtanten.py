def getSum(children):
    n = len(children)
    s = 0
    for i in range(n):
        s += (i+1) * children[i]
    return s

n = input()
children = list(map(int, input().split()))
children.remove(0)
children.insert(0, 0) #insert 0 person at front
curStart = getSum(children)
maxHappiness = curStart
curHappiness = curStart
curIdx = 0 #index of 0 person
while curIdx < len(children) - 1:
    if curHappiness > maxHappiness:
        maxHappiness = curHappiness
    #swap the 0 person with person next to him
    children[curIdx], children[curIdx + 1] = children[curIdx + 1], children[curIdx]
    curHappiness -= children[curIdx]
    curIdx += 1
if curHappiness > maxHappiness:
    maxHappiness = curHappiness
print(maxHappiness)

