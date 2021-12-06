import queue
INF = 1e9
class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id
    def __lt__(self, other):
        return self.dist <= other.dist
INF = 1001
graph = [[] for i in range(INF)]
dist = [INF for i in range(INF)]
path = [-1 for i in range(INF)]
visited = [False for i in range(INF)]
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
    return ans

t = int(input())
for i in range(t):
    p = int(input())
    n = int(input())
    m = int(input())
    for j in range(m):
        a, b, c = map(int, input().split())
        graph[a-1].append(Node(b-1, c))
        graph[b-1].append(Node(a-1, c))
    prims(0)
    ans = printMST() * p
    print(ans)
    graph = [[] for i in range(INF)]
    dist = [INF for i in range(INF)]
    path = [-1 for i in range(INF)]
    visited = [False for i in range(INF)]
        
