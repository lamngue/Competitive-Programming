n = int(input())
a = list(map(int,input().split()))

copy = list(a)
a.sort(reverse = True)
lenSoFar = 0
if (n==1):
    print(1)
else:
    rank = {}
    rank[a[0]] = 1
    lenSoFar = 1
    for i in range(1, n):
        if (a[i] - a[i-1] != 0):
            rank[a[i]] = 1 + lenSoFar
            lenSoFar += 1
        else:
            rank[a[i]] = rank[a[i-1]]
            lenSoFar += 1
    for i in range(n):
        print(rank[copy[i]], end=" ")


