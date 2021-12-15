from queue import Queue

t = int(input())
def BFS(s):
    pilot = 0
    q = Queue()
    visited[s] = True
    q.put(s)
    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                pilot += 1
                q.put(v)
    return pilot
                
for i in range(t):
    n, m = map(int, input().split())
    visited = [False for i in range(n)]
    dist = [0 for i in range(n)]
    graph = [[] for i in range(n)]
    for i in range(m):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    pilot = BFS(0)
    print(pilot)
