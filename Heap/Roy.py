import heapq
n = int(input())

class PQEntry:
    def __init__(self, ID, newZ, change):
        self.ID = ID
        self.newZ = newZ
        self.change = change
    def __lt__(self, other):
        return self.change > other.change or (self.change == other.change and self.ID > other.ID)

changes = []
for i in range(n):
    ID, Z, P, L, C, S = map(int, input().split())
    newZ = 50*P + 5*L + 10*C + 20*S
    change = newZ - Z

    heapq.heappush(changes,PQEntry(ID, newZ, change))
for i in range(5):
    x = heapq.heappop(changes)
    print(x.ID, x.newZ)
