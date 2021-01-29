import heapq

q = int(input())

heap = []
delete = []
for i in range(q):
    a = list(map(int, input().split()))
    if (a[0] == 1):
        heapq.heappush(heap, a[1])
        delete.append(a[1])
    elif (a[0] == 2):
        delete.remove(a[1])
    elif (a[0] == 3):
        while heap[0] not in delete:
            heapq.heappop(heap)
        print(heap[0])
