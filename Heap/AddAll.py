import heapq

while True:
    n = int(input())
    if (n == 0):
        break
    a = list(map(int,input().split()))
    heapq.heapify(a)
    cost = 0
    total =0
    while len(a) > 1:
        first = heapq.heappop(a)
        second = heapq.heappop(a)
        cost = first + second
        total += cost
        heapq.heappush(a,cost)
    print(total)
