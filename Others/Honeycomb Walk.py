
comb = [[[0 for col in range(30)]for row in range(30)] for x in range(30)]
dx = [-1, 0, 1, 1, 0, -1]
dy = [-1, -1, 0, 1, 1, 0]
def walk(x, y, step):
    if step == 0:
        if x == 0 and y == 0:
            return 1
        else:
            return 0
    if comb[x+14][y+14][step] != 0:
        return comb[x+14][y+14][step]

    out = 0
    for i in range(6):
        out += walk(x+dx[i], y+dy[i], step-1)            
    comb[x+14][y+14][step] = out
    return out

t = int(input())
for i in range(t):
    n = int(input())
    comb = [[[0 for col in range(30)]for row in range(30)] for x in range(30)]
    print(walk(0, 0, n))
    
