import queue

MAX = 20000
INF = int(1e9)
graph = [[] for i in range(MAX)]
dist = [INF for i in range(MAX)]

class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id
    def __lt__(self, other):
        return self.dist <= other.dist


def Dijkstra(s):
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
                


q = int(input())
for i in range(q):
    n, m, s, t = map(int, input().split())
    for j in range(m):
        a, b, w = map(int, input().split())
        graph[a].append(Node(b, w))
        graph[b].append(Node(a,w))
    Dijkstra(s)
    if (dist[t] >= INF):
        print("Case #" + str(i+1) + ": unreachable")
    else:
        print("Case #" + str(i+1) + ": " + str(dist[t]))
    graph = [[] for i in range(MAX)]
    dist = [INF for i in range(MAX)]
