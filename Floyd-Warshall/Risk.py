MAX = 100
INF = int(1e9)
def FloydWarshall(graph, dist):
    for i in range(20):
        for j in range(20):
            dist[i][j] = graph[i][j]
    for k in range(20):
        for i in range(20):
            for j in range(20):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    for i in range(20):
        if dist[i][i] < 0:
            return True
    return False
s = 1
while True:
    try:
        graph = [[INF for i in range(20)] for j in range(20)]
        dist = [[None for i in range(20)] for j in range(20)]
        line = 0
        while (line < 19):
            inp = list(map(int, input().split()))
            border = inp[0]
            for i in range(1, border + 1):
                graph[line][inp[i] - 1] = 1
                graph[inp[i] - 1][line] = 1
            line += 1
        FloydWarshall(graph, dist)
        t = int(input())
        print("Test Set #" + str(s))
        s += 1
        for i in range(t):
            f, t = map(int, input().split())
            if f < 10:
                f = ' ' + str(f)
            if t < 10:
                t = ' ' + str(t)
            else:
                f = str(f)
                t = str(t)
            print(str(f) + " to " + str(t) + ": " + str(dist[int(f)-1][int(t)-1]))
        print("")
    except EOFError:
        break
    
