n, m = map(int, input().split())
graph = [[] for i in range(n)]
visited = [False for i in range(n)]
def DFS(src):
    visited = [False for i in range(n)]
    s = []
    dis = 1
    visited[src] = True
    s.append(src)
    while len(s) > 0:
        u = s.pop()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                dis += 1
                s.append(v)
    return dis

for i in range(m):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
m = 0
maxSoFar = 0
for i in range(n):
    if not visited[i]:
        maxSoFar = DFS(i)
    m = max(m, maxSoFar)
print(m)
