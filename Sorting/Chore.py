f = input().split()
n = int(f[0])
a = int(f[1])
b = int(f[2])


c = list(map(int,input().split()))

c.sort()
print(c[b] - c[b-1])
