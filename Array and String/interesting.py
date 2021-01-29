n = int(input())
interesting = list(map(int,input().split()))


def minutes(n, interesting):
    total = 0
    # [7, 20, 88] -> 35 cause 20-7 = 13 < 15, 88 - 20 = 68 > 15 so stopped at 35 mins
    if (interesting[0] > 15):
        return 15
    lastWatch = 0;
    for i in range(n):
        lastWatch += 1
        if (i < n-1 and interesting[i+1] - interesting[i] > 15):
            break
    lastWatch -= 1
    if lastWatch == n-1 and interesting[lastWatch] + 15 > 90:
        return 90
    return interesting[lastWatch] + 15

print(minutes(n,interesting))
