class Node:
    def __init__(self):
        self.child = dict()
        self.isEnd = False
def addWord(root, s, flag):
    temp = root
    for ch in s:
        if ch not in temp.child:
            temp.child[ch] = Node()
        temp = temp.child[ch]
        if (temp.isEnd):
            flag = True
    for i in range(10):
        if str(i) in temp.child:
            flag = True
            break
    temp.isEnd = True
    return flag


t = int(input())
for i in range(t):
    root = Node()
    n = int(input())
    flag = False
    fin = False
    for j in range(n):
        number = input()
        res = addWord(root, number, flag)
        if (res):
            fin = True
    if (not fin):
        print("Case " + str(i+1) + ": YES" )
    else:
        print("Case " + str(i+1) + ": NO")
        
