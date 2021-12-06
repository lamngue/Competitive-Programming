from collections import deque
s = str(input())
n = len(s)
allLower = True
for i in range(n):
    if s[i].isupper():
        allLower = False
cursor = 0
stack = []
out = ""
if allLower:
    print(s)
#iLnLnLeLb
else:
    for i in range(n):
        if s[i] == "L":
            cursor -= 1
        elif s[i] == "R":
            cursor += 1
        elif s[i] == "B":
            stack.pop(cursor-1)
            cursor -= 1
        else:
            stack.insert(cursor, s[i])
            cursor += 1
    print(''.join(stack))
