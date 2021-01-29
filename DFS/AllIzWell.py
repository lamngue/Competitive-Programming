t = int(input())

sentence = "ALLIZZWELL"

def notOutOfBound(x, y, r, c):
    return x >= 0 and y >= 0 and x < c and y < r
dr = [1,-1,0,1,-1, 1, -1, 0]
dc = [1,1,1, 0, 0, -1, -1,-1]

def DFS(x, y, ID):
    if (ID == 10):
        return True
    visited[y][x] = True
    for i in range(8):
        row = y + dr[i]
        col = x + dc[i]
        if (notOutOfBound(col, row, r,c) and not visited[row][col]
            and graph[row][col] == sentence[ID]):
            check = DFS(col, row, ID + 1)
            if (check):
                return True
    visited[y][x] = False
    return False
            
for i in range(t):
    r, c = map(int, input().split())
    graph = [['' for i in range(c)] for i in range(r)]
    visited = [[False for i in range(c)] for i in range(r)]
    startX = 0
    startY = 0
    flag = False
    for j in range(r):
        line = list(input())
        for k in range(c):
            visited[j][k] = False
            graph[j][k] = line[k]
    for j in range(r):
        for k in range(c):
            if graph[j][k] == 'A':
                startX = k
                startY = j
                ID = DFS(startX, startY, 1)
                if (ID):
                    flag = True
                    break
    if (flag):
        print("YES")
    else:
        print("NO")
    if i < t-1:
        input()
