t = int(input())


def checkCycle(n):
    if visited[n]:
        return False
    if explore[n]:
        return True
    explore[n] = True
    for v in graph[n]:
        if not visited[v]:
            cycle = checkCycle(v)
            if (cycle):
                return True
    #backtrack
    explore[n] = False
    visited[n] = True
    return False

for i in range(t):
    n, m = map(int, input().split())
    visited = [False for i in range(n)]
    explore = [False for i in range(n)]
    graph = [[] for i in range(n)]
    path = [-1 for i in range(n)]
    cycle = False
    for i in range(m):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
    for i in range(n):
        cycle = checkCycle(i-1)
        if (cycle):
            print("YES")
            break
    else:
        print("NO")
