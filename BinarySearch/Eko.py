

n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()
left = 0
right = trees[n-1]
ans = 0
def getTotal(ans):
    total = 0
    for i in range(n):
        if trees[i] - ans > 0:
            total += trees[i] - ans 
    return total

while left <= right:
    mid = (left + right) // 2
    if getTotal(mid) >= m:
        ans = mid
        left = mid + 1
    elif getTotal(mid) < m:
        right = mid - 1
print(ans)
    
    
