t = int(input())

def testK(k, rungs):
    for i in range(1, len(rungs)):
        if rungs[i] - rungs[i-1] > k:
            return False
        elif rungs[i] - rungs[i-1] == k:
            k -= 1
    return True

for i in range(t):
    n = int(input())
    rungs = list(map(int, input().split()))
    ans = rungs[n-1]
    left = rungs[0]
    right = rungs[n - 1]
    while left <= right:
        mid = (left + right) // 2
        if testK(mid, rungs):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    print("Case " + str(i + 1) + ": " + str(ans))
