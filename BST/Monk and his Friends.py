from collections import defaultdict
t = int(input())


for i in range(t):
    n, m = map(int, input().split())
    candies = list(map(int, input().split()))
    inClass = candies[:n]
    outClass = candies[n:]
    s = set(inClass)
    for j in range(m):
        if outClass[j] in s:
            print("YES")
        else:
            print("NO")
        s.add(outClass[j])
        
