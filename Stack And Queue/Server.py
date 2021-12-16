n, T = map(int, input().split())
tasks = list(map(int, input().split()))
s = 0
c = 0
for i in range(n):
    if s + tasks[i] > T:
        break
    s += tasks[i]
    c += 1
print(c)
