from queue import Queue
MAX = 100000

visited = [False for i in range(MAX)]
dist = [0 for i in range(MAX)]
graph = [[] for i in range(MAX)]

def BFS(s):
    q = Queue()
    visited[s] = True
    q.put(s)
    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if not visited[v]:
                dist[v] = dist[u] + 1
                visited[v] = True
                q.put(v)



n, m = map(int, input().split())
for i in range(m):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

BFS(0)
print(dist[n-1] - 1)
