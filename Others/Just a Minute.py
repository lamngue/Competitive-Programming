n = int(input())
avg = 0
totalS = 0
totalM = 0
for i in range(n):
    m, s = map(int, input().split())
    totalS += s
    totalM += m
if totalS / (totalM * 60) <= 1:
    print("measurement error")
else:
    print(round(totalS / (totalM * 60), 7))
