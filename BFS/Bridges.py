from collections import deque
INF = int(1e9)
n, m = map(int, input().split())
visited = [False for i in range(n)]
dist = [INF for i in range(n)]
graph = [[] for i in range(n)]

class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id
    def __lt__(self, other):
        return self.dist <= other.dist
def BFS01(s):
    dist[s] = 0
    q = deque()
    q.appendleft(s)
    while (len(q) != 0):
        v = q.popleft()
        for e in graph[v]:
            u = e.id
            w = e.dist
            if dist[v] + w < dist[u]:
                dist[u] = dist[v] + w
                if w == 1:
                    q.append(u)
                else:
                    q.appendleft(u)


for i in range(m):
    a, b, c = map(int, input().split())
    graph[a-1].append(Node(b-1, c))
    graph[b-1].append(Node(a-1, c))

BFS01(0)
print(dist[n-1])

