
def makeSet(r):
    global parent, ranks, cnt
    parent = [i for i in range(r + 1)]
    ranks = [0 for i in range(r + 1)]
    cnt = r
    
def findSet(u):
    while u != parent[u]:
        u = parent[u]
    return u
 
def unionSet(u, v, cnt):
    up = findSet(u)
    vp = findSet(v)
    if vp != up:
        if ranks[up] < ranks[vp]:
            parent[up] = vp
        else:
            parent[vp] = up
            if ranks[up] == ranks[vp]:
                ranks[up] += 1
        return True
    return False
        

t = int(input())
for i in range(t):
    input()
    c = input()
    makeSet(ord(c) - 64)
    ans = ord(c) - 64
    while True:
        try:
            s = input()
            a = ord(s[0]) - 64
            b = ord(s[1]) - 64
            res = unionSet(a, b, cnt)
            if (res):
            	ans -= 1
        except EOFError:
            break
    print(ans)
    print()
    
# your code goes here
