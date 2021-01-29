import heapq
n = int(input())

class PQEntryMin:
    def __init__(self, value):
        self.value = value
    def __lt__(self, other):
        return self.value < other.value

class PQEntryMax:
    def __init__(self, value):
        self.value = value
    def __lt__(self, other):
        return self.value > other.value

maxR = []
minR = []
ID = 0
for i in range(n):
    a = list(map(int, input().split()))
    if a[0] == 1:
        heapq.heappush(maxR, PQEntryMax(a[1]))
        ID += 1
        if (ID % 3 == 0):
            heapq.heappush(minR, PQEntryMin(heapq.heappop(maxR).value))
        elif (len(minR) > 0 and maxR[0].value > minR[0].value):
            #swap values
            heapq.heappush(minR, PQEntryMin(heapq.heappop(maxR).value))
            heapq.heappush(maxR, PQEntryMax(heapq.heappop(minR).value))
    elif a[0] == 2:
        if (ID < 3):
            print("No reviews yet")
        else:
            print(minR[0].value)
