n, k = map(int, input().split())
e = list(map(int, input().split()))

e.sort()
def transfer(power):
    received, given = 0, 0
    for i in range(n):
        if (e[i] < power):
            received += power - e[i]
        else:
            given += (e[i] - power)
    return given - (given * k)/100 >= received

left = e[0]
right = e[n-1]
ans = 0
while right - left > 1e-7:
    mid = (left + right) / 2
    if transfer(mid):
        left = mid 
    else:
        right = mid 
print("{:.9f}".format(left))
