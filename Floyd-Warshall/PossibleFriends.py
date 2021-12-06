MAX = 100
INF = int(1e9)
def FloydWarshall(dist):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

t = int(input())
for i in range(t):
    line = input()
    n = len(line)
    matrix = [None for i in range(n)]
    dist = [[None for i in range(n)] for i in range(n)]
    matrix[0] = line
    for i in range(1, n):
        line = input()
        matrix[i] = line
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 'Y':
                dist[i][j] = 1
            else:
                dist[i][j] = INF
        dist[i][i] = 0
    FloydWarshall(dist)
    nfriends = 0
    index = 0
    for i in range(n):
        count = 0
        for j in range(n):
            if dist[i][j] == 2: #mutual friends
                count += 1
        if count > nfriends:
            nfriends = count
            index = i
    print(str(index) + ' ' + str(nfriends))
    matrix = [None for i in range(n)]
    dist = [[None for i in range(n)] for i in range(n)]
