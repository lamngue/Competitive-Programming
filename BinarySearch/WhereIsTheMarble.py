def binarySearch(a, left, right, x):
    if left <= right:
        mid = (left + right) // 2
        if (mid == left or x > a[mid-1]) and a[mid] == x:
            return mid
        elif x > a[mid]:
            return binarySearch(a, mid+1, right,x)
        else:
            return binarySearch(a, left, mid-1,x)
    return -1

c = 1
while True:
    n, q = map(int, input().split())
    if n == 0 and q == 0:
        break
    marbles = []
    for i in range(n):
        marbles.append(int(input()))
    marbles.sort()
    print("CASE# " + str(c) + ":")
    for i in range(q):
        m = int(input())
        f = binarySearch(marbles, 0, len(marbles) - 1, m)
        if f == -1:
            print(str(m) + " not found")
        else:
            print(str(m) + " found at " + str(f+1))
    c += 1
