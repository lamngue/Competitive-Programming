n = int(input())
heights = list(map(int, input().split()))
chimps = []
last = -1
for i in range(n):
    if heights[i] != last:
        chimps.append(heights[i])
        last = heights[i]
q = int(input())
luchu = list(map(int, input().split()))
def binarySearch(a, n, x):
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        el_mid = a[mid]
        if x == el_mid:
            return mid-1, mid+1
        elif el_mid < x:
            left = mid + 1
        else:
            right = mid - 1
    return right, left
n = len(chimps)
for i in range(q):
    lower, upper = binarySearch(chimps, n, luchu[i])
    outLow = chimps[lower] if lower >= 0 else "X"
    outHigh = chimps[upper] if upper < n else "X"
    print(str(outLow), str(outHigh))
    
