t = int(input())

def DFS(src):
    s = []
    dis = 0
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

for i in range(t):
    n = int(input())
    e = int(input())
    if (e == 0):
        print(n)
    else:
        MAX = 100001
        visited = [False for i in range(MAX)]
        path = [-1 for i in range(MAX)]
        graph = [[] for i in range(n)]
        for i in range(e):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)
        #count single node
        single = 0
        for i in range(n):
            if (len(graph[i]) == 0):
                single += 1
        
        m = 0
        for i in range(n):
            if (len(graph[i]) > 0):
                maxSoFar = DFS(i)
                if (maxSoFar > 0):
                    m += 1
        print(m + single)
