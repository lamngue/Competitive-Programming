class Node:
    def __init__(self):
        self.countWord = 0
        self.isEnd = False
        self.child = dict()
    def __repr__(self):
         return "{countWord: %s, isEnd: %s, child: %s}" % (self.countWord, self.isEnd, self.child)
    def __str__(self):
         return "{countWord: %s, isEnd: %s, child: %s}" % (self.countWord, self.isEnd, self.child)
string = "abcdefghij"       
def addWord(root, s, flag):
    temp = root
    for ch in s:
        if ch not in temp.child:
            temp.child[ch] = Node()
        temp = temp.child[ch]
        if (temp.isEnd):
            flag = True
    for i in range(10):
        if string[i] in temp.child:
            flag = True
            break
    temp.isEnd = True
    return flag

n = int(input())
strs = []
root = Node()
flag = False
fin = False
out = None
for i in range(n):
    s = input()
    strs.append(s)
for j in range(n):
    res = addWord(root, strs[j], flag)
    if (res):
        fin = True
        out = strs[j]
        break
if (not fin):
    print("GOOD SET" )
else:
    print("BAD SET")
    print(out)
