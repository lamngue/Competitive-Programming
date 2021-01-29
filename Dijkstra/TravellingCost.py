import queue
MAX = 501
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
                path[neighbor.id] = u
                       
n = int(input())
for i in range(n):
    a, b, w = map(int, input().split())
    graph[a].append(Node(b, w))
    graph[b].append(Node(a,w))
s = int(input())
Dijkstra(s)
q = int(input())
for j in range(q):
    t = int(input())
    if (dist[t] == INF):
        print("NO PATH")
    else:
        print(dist[t])
