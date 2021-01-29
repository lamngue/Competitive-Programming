f = input().split()
n = int(f[0])
m = int(f[1])
x = int(f[2])
y = int(f[3])
d = list(map(int,input().split()))
a = list(map(int,input().split()))


k = 0
soldier = []
vest = []
i = 0
j = 0
while i < n and j < m:
    if (j < len(a) and d[i] - x <= a[j] and a[j] <= d[i] + y):
       soldier.append(i + 1)
       vest.append(j+1)
       i += 1
       j += 1
       k += 1
    elif d[i] - x > a[j]:
        j += 1
    else:
        i += 1

print(k)
for i in range(k):
    print(soldier[i], vest[i])
