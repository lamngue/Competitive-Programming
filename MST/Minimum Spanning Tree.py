import queue
INF = 1001
graph = [[] for i in range(INF)]
dist = [INF for i in range(INF)]
path = [-1 for i in range(INF)]
visited = [False for i in range(INF)]
class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id
    def __lt__(self, other):
        return self.dist <= other.dist

def prims(src):
    pq = queue.PriorityQueue()
    pq.put(Node(src, 0))
    dist[src] = 0
    while pq.empty() == False:
        top = pq.get()
        u = top.id
        visited[u] = True
        for neighbor in graph[u]:
            v = neighbor.id
            w = neighbor.dist
            if visited[v] == False and w < dist[v]:
                dist[v] = w
                pq.put(Node(v, w))
                path[v] = u

def printMST():
    ans = 0
    for i in range(n):
        if path[i] == -1:
            continue
        ans += dist[i]
    print(ans)

n, m = map(int, input().split())
graph = [[] for i in range(n)]
dist = [INF for i in range(n)]
path = [-1 for i in range(n)]
visited = [False for i in range(n)]
for i in range(m):
    u, v, w = map(int, input().split())
    graph[u-1].append(Node(v-1, w))
    graph[v-1].append(Node(u-1, w))
prims(0)
printMST()
