f = input().split()
n = int(f[0])
k = int(f[1])
a = list(map(int,input().split()))

#if the set from array is smaller than k, print -1:
if (len(set(a)) < k):
    print(-1, -1)
else:
    s = set()
    t = set()
    i = 0
    g = 0
    for j in range(len(a)):
        t.add(a[j])
        if len(t) == k:
            g = j
            break
    for j in range(g, 0, -1):
        s.add(a[j])
        if len(s) == k:
            i = j
            break
    print(i+1, g+1)

    
