import queue

MAX = 10000
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
                

s = int(input())
idx = []
for i in range(s):
    n = int(input()) #number of cities
    for i in range(n):
        name = input()
        idx.append(name)
        p = int(input()) #neighbors
        for j in range(p):
            nr, cost = map(int, input().split())
            graph[i].append(Node(nr-1, cost))
    r = int(input())
    for k in range(r):
        name1, name2 = map(str, input().split())
        start = idx.index(name1)
        end = idx.index(name2)
        Dijkstra(start)
        print(dist[end])
        dist = [INF for i in range(MAX)]
    graph = [[] for i in range(MAX)]
    idx = []
    input()
