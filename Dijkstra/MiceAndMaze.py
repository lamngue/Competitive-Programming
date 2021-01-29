import queue

MAX = 101
INF = int(1e9)
graph = [[] for i in range(MAX)]
dist = [INF for i in range(MAX)]
path = [-1 for i in range(MAX)]
class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id
    def __lt__(self, other):
        return self.dist <= other.dist

def Dijkstra(s, f):
    dist = [INF for i in range(MAX)]
    pq = queue.PriorityQueue()
    pq.put(Node(s, 0))
    dist[s] = 0
    while pq.empty() == False:
        top = pq.get()
        u = top.id
        w = top.dist
        for neighbor in graph[u]:
            if w + neighbor.dist < dist[neighbor.id]:
                dist[neighbor.id] = w + neighbor.dist
                pq.put(Node(neighbor.id, dist[neighbor.id]))
                path[neighbor.id] = u
    return dist[f]
                       
n = int(input())
e = int(input()) - 1
t = int(input())
m = int(input())
for i in range(m):
    a, b, w = map(int, input().split())
    graph[a-1].append(Node(b-1, w))
c = 0
for i in range(n):
    d = Dijkstra(i, e)
    if (d <= t or i == e):
        c += 1
print(c)
