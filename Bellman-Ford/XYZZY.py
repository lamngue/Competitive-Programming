INF = 10**9
MAX = 101

class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight
    def setWeight(self, weight):
        self.weight = weight
    def __repr__(self):
         return "{source: %s, target: %s, weight: %s}" % (self.source, self.target, self.weight)
    def __str__(self):
        return "{source: %s, target: %s, weight: %s}" % (self.source, self.target, self.weight)

    
dist = [INF for _ in range(MAX)]
path = [-1 for _ in range(MAX)]
graph = []

def BellmanFord(s):
    dist[s] = 0
    for i in range(1, n):
        for j in range(m):
            u = graph[j].source
            v = graph[j].target
            w = graph[j].weight
            if (dist[u] != INF) and (dist[u] + w < dist[v]) and dist[u] + w < 100:
                dist[v] = dist[u] + w
                path[v] = u
    for i in range(m):
        u = graph[i].source
        v = graph[i].target
        w = graph[i].weight
        #Check negative cycle
        if (dist[u] != INF) and (dist[u] + w < dist[v]) and dist[u] + w < 100:
            dist[v] = -INF

while True:
    n = int(input())
    m = 0
    weights = []
    if n == -1:
        break
    for r in range(n):
        line = list(map(int, input().split()))
        w = line[0]
        doors = line[1]
        weights.append(w)
        for d in range(doors):
            v = line[2 + d]
            m += 1
            graph.append(Edge(r, v-1, 0))
    for i in range(m):
        start = graph[i].source
        target = graph[i].target
        weight = weights[target]
        graph[i].setWeight(-weight)
    s = 0
    BellmanFord(s)
    if dist[n-1] == INF or dist[n-1] >= 100:
        print("hopeless")
    else:
        print("winnable")
    dist = [INF for _ in range(MAX)]
    path = [-1 for _ in range(MAX)]
    graph = []

