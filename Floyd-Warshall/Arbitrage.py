MAX = 100
INF = int(1e9)
def FloydWarshall(graph, dist):
    for i in range(n):
        for j in range(n):
            dist[i][j] = graph[i][j]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = max(dist[i][j], dist[i][k] * dist[k][j])
    for i in range(n):
        if dist[i][i] > 1:
            return True
    return False
c = 0
while True:
    c += 1
    n = int(input())
    if n == 0:
        break
    nodes = []
    for i in range(n):
        currency = input()
        nodes.append(currency)
    graph = [[0 for i in range(n)] for j in range(n)]
    dist = [[None for i in range(n)] for j in range(n)]
    m = int(input())
    for i in range(m):
        line = input().split()
        u = nodes.index(line[0])
        w = float(line[1])
        v = nodes.index(line[2])
        graph[u][v] = w
    res = FloydWarshall(graph, dist)
    if (not res):
        print("Case " + str(c) + ": No")
    else:
        print("Case " + str(c) + ": Yes")
    input()
        
