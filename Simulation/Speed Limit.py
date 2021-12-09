while True:
    n = int(input())
    if n == -1:
        break
    total = 0
    prev = 0
    for i in range(n):
        s, t = map(int, input().split())
        if i == 0:
            total = s * t
            prev = t
        else:
            total += s * (t - prev)
            prev = t
    print(str(total) + " miles")
        

