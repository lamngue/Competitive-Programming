t = int(input())
for i in range(t):
    n = int(input())
    s = sum(int(digit) for digit in str(n))
    cur = n - 1
    biggestSoFar = 0
    while cur > 0:
        subSum = sum(int(digit) for digit in str(cur))
        if s - subSum == 1:
            biggestSoFar = cur
            break
        cur -= 1
    print(biggestSoFar)
    
