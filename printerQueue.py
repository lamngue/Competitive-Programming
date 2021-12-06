import queue
import heapq
t = int(input())
class PQEntry:
    def __init__(self,ID, value):
        self.ID = ID
        self.value = value #priority
    def __lt__(self, other):
        return self.value > other.value


for i in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    q = queue.Queue()
    pq = queue.PriorityQueue()
    t = 0
    #put jobs
    for i in range(n):
        q.put(PQEntry(i, a[i]))
        pq.put(PQEntry(i, a[i]))
    while not q.empty():
        j = q.get()
        if (pq.queue[0].value == j.value):
            t += 1
            pq.get()
            if (j.ID == m):
                break
        else:
            q.put(j)
    print(t)
