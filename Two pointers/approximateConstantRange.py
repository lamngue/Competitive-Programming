n = int(input())
a = list(map(int,input().split()))


left = 0
maxLength = 0
distinct = 0
s = set()
count = [0] * 100005
for right in range(n):
    if count[a[right]] == 0:
        distinct += 1
    count[a[right]] += 1
    while (distinct > 2):
        count[a[left]] -= 1
        if (count[a[left]] == 0):
            distinct -= 1
        left += 1
    len = right-left+1
    maxLength = max(maxLength, right-left+1)
print(maxLength)

##traversed = []
##i = 0
##maxSize = 0
##def remove(l, v):
##    return [val for val in l if val != v]
##
##while i < n:
##    traversed.append(a[i])
##    k = len(traversed)
##    if (abs(traversed[0]-traversed[k-1]) > 1):
##        traversed = remove(traversed, traversed[0])
##    maxSize = max(maxSize, len(traversed))
##    i += 1
##print(maxSize)
##    

        
