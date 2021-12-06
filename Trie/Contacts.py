class Node:
    def __init__(self):
        self.countWord = 0
        self.isEnd = False
        self.child = dict()
    def __repr__(self):
         return "{countWord: %s, isEnd: %s, child: %s}" % (self.countWord, self.isEnd, self.child)
    def __str__(self):
         return "{countWord: %s, isEnd: %s, child: %s}" % (self.countWord, self.isEnd, self.child)
def addWord(root, s):
    temp = root
    for ch in s:
        if ch not in temp.child:
            temp.child[ch] = Node()
        temp = temp.child[ch]
        temp.countWord += 1
    temp.isEnd = True

def findWord(root, s):
    temp = root
    cnt = 0
    for ch in s:
        if ch not in temp.child:
            return 0
        temp = temp.child[ch]
    return temp.countWord

def isWord(node):
    return node.countWord != 0

def isEmpty(node):
    return len(node.child) == 0

n = int(input())
root = Node()
for i in range(n):
    name, partial = map(str, input().split())
    cnt = 0
    if name == 'add':
        addWord(root, partial)
    else:
        res = findWord(root, partial)
        print(res)
