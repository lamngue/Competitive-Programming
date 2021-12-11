n = int(input())
bricks = list(map(int, input().split()))
count = 1
for i in range(n):
    if bricks[i] > bricks[i-1] and i > 0:
        count += 1
print(count)
