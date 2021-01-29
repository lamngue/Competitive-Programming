f = input().split()
n = int(f[0])
x = int(f[1])
a = list(map(int,input().split()))

t = 0
a.sort()
for i in range(n):
    t += a[i] * x
    if i>= 0 and x > 1:
        x = x - 1
    print(t)

