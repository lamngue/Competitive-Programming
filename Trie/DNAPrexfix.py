class Node:
    def __init__(self):
        self.countWord = 0
        self.child = dict()
def addWord(root, s, ans):
    temp = root
    i = 0 #level
    for ch in s:
        if ch not in temp.child:
            temp.child[ch] = Node()
        temp = temp.child[ch]
        temp.countWord += 1
        i += 1
        ans = max(ans, i*temp.countWord)
    return ans
t = int(input())
for i in range(t):
    s = int(input())
    root = Node()
    ans = 0
    for j in range(s):
        dna = input()
        ans = addWord(root, dna, ans)
    print("Case " + str(i+1) + ": " + str(ans))
