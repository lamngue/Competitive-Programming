import heapq
n = int(input())
class PQEntryMin:
    def __init__(self,ID, value):
        self.ID = ID
        self.value = value
    def __lt__(self, other):
        return self.value < other.value

class PQEntryMax:
    def __init__(self,ID, value):
        self.ID = ID
        self.value = value
    def __lt__(self, other):
        return self.value > other.value
    

minHeap = []
maxHeap = []
MAX = 100000
visited = [False for i in range(MAX)]
total = 0
ID = 0
for i in range(n):
    l = list(map(int, input().split()))
    for j in range(1, l[0]+1):
        heapq.heappush(minHeap, PQEntryMin(ID, l[j]))
        heapq.heappush(maxHeap, PQEntryMax(ID, l[j]))
        ID += 1
    higher = heapq.heappop(maxHeap)
    lower = heapq.heappop(minHeap)
    if (visited[higher.ID]):
        higher = heapq.heappop(minHeap)
    else:
        visited[higher.ID] = True
    if (visited[lower.ID]):
        lower = heapq.heappop(maxHeap)
    else:
        visited[lower.ID] = True
    cost = higher.value - lower.value
    total += cost
print(total)
