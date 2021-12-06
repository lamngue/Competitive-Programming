INF = 10**9
MAX = 101

class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight
    def __repr__(self):
         return "{source: %s, target: %s, weight: %s}" % (self.source, self.target, self.weight)
    def __str__(self):
        return "{source: %s, target: %s, weight: %s}" % (self.source, self.target, self.weight)

dist = [INF for _ in range(MAX)]
graph = []

def BellmanFord(s):
    dist[s] = 0
    for i in range(1, n):
        for j in range(m):
            u = graph[j].source
            v = graph[j].target
            w = graph[j].weight
            if (dist[u] != INF) and (dist[u] + w < dist[v]):
                dist[v] = dist[u] + w
    for i in range(m):
        u = graph[i].source
        v = graph[i].target
        w = graph[i].weight
        if (dist[u] != INF) and (dist[u] + w < dist[v]):
            return False
    return True
            
t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    for i in range(m):
        u, v, w = map(int, input().split())
        graph.append(Edge(u- 1, v - 1, w))
    res = BellmanFord(0)
    if (not res):
        print("Yes")
    else:
        print("No")
    graph = []
    dist = [INF for _ in range(MAX)]
