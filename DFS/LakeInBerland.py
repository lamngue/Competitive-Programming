n, m, k = map(int, input().split())
table = [['' for i in range(m)] for i in range(n)]
visited = [[False for i in range(m)] for i in range(n)]

class Prop:
    def __init__(self, size, x, y):
        self.size = size
        self.x = x
        self.y = y
    def __lt__(self, other):
        if (self.size < other.size):
            return True
        return False
        

def notOutOfBound(x, y, n, m):
    return x > 0 and y > 0 and x < m-1 and y < n-1

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
lakes = []
def DFS(sr, sc):
    s = [(sr, sc)]
    visited[sr][sc] = True
    isOcean = False
    temp = []
    while len(s):
        ur, uc = s.pop()
        temp.append((ur, uc))

        if ur == 0 or uc == 0 or ur == n - 1 or uc == m - 1:
            isOcean = True
        
        for i in range(4):
            r = ur + dr[i]
            c = uc + dc[i]

            if r in range(n) and c in range(m) and table[r][c] == '.' and not visited[r][c]:
                visited[r][c] = True
                s.append((r, c))
    
    if not isOcean:
        lakes.append(temp)

def DFSFill(x, y):
    visited = [[False for i in range(m)] for i in range(n)]
    for i in range(4):
        row = y + dr[i]
        col = x + dc[i]
        if (notOutOfBound(col, row, n,m) and not visited[row][col]
            and table[row][col] == '.'):
             visited[row][col] = True
             table[row][col] = '*'
             DFSFill(col, row)
    

for i in range(n):
    line = list(input())
    for j in range(m):
        table[i][j] = line[j]
lakes = []
for i in range(n):
    for j in range(m):
        if (table[i][j] == '.'
            and visited[i][j] == False):
            DFS(i, j)
lakes.sort(key=lambda lake: len(lake))
lakes = lakes[:len(lakes)-k]
    
#count cell to fill
cell = 0
for i in range(len(lakes)):
    cell += len(lakes[i])
    for r, c in lakes[i]:
        table[r][c] = '*'
print(cell)
for r in table:
    for c in r:
        print(c,end = "")
    print()
        
