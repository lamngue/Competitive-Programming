
def makeSet(r):
    global parent, ranks, cnt
    parent = [i for i in range(r + 5)]
    ranks = [0 for i in range(r + 5)]
    cnt = r
    
def findSet(u):
    while u != parent[u]:
        u = parent[u]
    return u
 
def unionSet(u, v):
    up = findSet(u)
    vp = findSet(v)
    if vp != up:
        if ranks[up] < ranks[vp]:
            parent[up] = vp
        else:
            parent[vp] = up
            if ranks[up] == ranks[vp]:
                ranks[up] += 1
        cnt -= 1
    return cnt

t = int(input())
for i in range(t):
    input()
    c = input()
    makeSet(ord(c) - 65)
    ans = None
    while True:
        try:
            s = input()
            a = ord(s[0]) - 65
            b = ord(s[1]) - 65
            ans = unionSet(a, b)
        except EOFError:
            break
    print(ans)
    print()
    
# your code goes here
