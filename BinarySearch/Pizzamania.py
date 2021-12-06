t = int(input())
def binarySearch(a, left, right, x):
    while left <= right:
        mid = (left + right) // 2
        if x == a[mid]:
            return mid
        elif x < a[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1
for i in range(t):
    n, m = map(int, input().split())
    money = list(map(int, input().split()))
    money.sort()
    j = 0
    pair = 0
    while j < n:
        f = money[j]
        s = binarySearch(money, 0, n-1, m-f)
        if (s != -1):
            pair += 1
        j += 1
    print(int(pair/2))
        
        
