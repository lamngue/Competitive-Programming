INF = 10**9
MAX = 201

class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight
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
            if (dist[u] != INF) and (dist[u] + w < dist[v]):
                dist[v] = dist[u] + w
                path[v] = u
    for i in range(m):
        u = graph[i].source
        v = graph[i].target
        w = graph[i].weight
        if (dist[u] != INF) and (dist[u] + w < dist[v]):
            dist[v] = -INF

t = int(input())
for c in range(t):
    input()
    n = int(input())
    junctions = list(map(int, input().split()))
    m = int(input())
    for i in range(m):
        u, v = map(int, input().split())
        w = (junctions[v-1] - junctions[u-1])**3
        graph.append(Edge(u-1, v-1, w))
    s = 0
    BellmanFord(s)
    q = int(input())
    print("Case " + str(c+1) + ":")
    for i in range(q):
        d = int(input())
        if dist[d-1] < 3 or dist[d-1] == INF or path[d-1] == -1:
            print("?")
        else:
            print(dist[d-1])
    dist = [INF for _ in range(MAX)]
    path = [-1 for _ in range(MAX)]
    graph = []        
        
