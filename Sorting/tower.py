n = int(input())
a = list(map(int,input().split()))

a.sort()

#[5,6,6,7]
count = [0] * 100
diff = 1
c = 1
maxC = 1
for i in range(1,n):
    if (a[i-1] != a[i]):
        diff += 1
        c = 1
    else:
        c += 1
        maxC = max(maxC,c)
        

print(maxC,diff)
