from collections import defaultdict
N, t = map(int, input().split())
arr = list(map(int, input().split()))
n = len(arr)
if t == 1:
    target = 7777
    dic = defaultdict(lambda: 0)
    flag = False
    for i in range(n):
        if dic[target - arr[i]] != 0 and arr[i] != target - arr[i]:
            flag = True
            break
        else:
            dic[arr[i]] = 1
    if (flag):
        print("Yes")
    else:
        print("No")
elif t == 2:
    if len(set(arr)) != n:
        print("Contains duplicate")
    else:
        print("Unique")
elif t == 3:
    arr.sort()
    el = arr[0]
    can = el
    vote = 0
    maxVote = vote
    found = False
    for i in range(n):
        if arr[i] == el:
            vote += 1
        else:
            el = arr[i]
            vote = 1
        if vote > n//2 and vote > maxVote:
            found = True
            can = el
            maxVote = vote
    if (found):
        print(can)
    else:
        print(-1)
elif t == 4:
    arr.sort()
    mid = n // 2
    if n % 2 == 1:
        print(arr[mid])
    else:
        for i in range(mid-1, mid+1):
            print(arr[i], end=" ")
else:
    arr.sort()
    for i in range(n):
        if arr[i] >= 100 and arr[i] <= 999:
            print(arr[i], end = " ")