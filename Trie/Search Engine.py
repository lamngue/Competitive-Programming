class Node:
    def __init__(self):
        self.countWord = -1
        self.child = dict()
        
def addWord(root, s, w):
    temp = root
    for ch in s:
        order = ord(ch) - 96
        if order not in temp.child:
            temp.child[order] = Node()
        temp = temp.child[order]
        temp.countWord = max(w, temp.countWord)
    
def findWord(root, s):
    temp = root
    for ch in s:
        order = ord(ch) - 96
        if order not in temp.child:
            return -1
        temp = temp.child[order]
    return temp.countWord

n, q = map(int, input().split())
root = Node()
for i in range(n):
    l = input().split()
    addWord(root, l[0], int(l[1]))
    
for i in range(q):
    s = input()
    print(findWord(root, s))
    
