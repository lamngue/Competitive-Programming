from collections import defaultdict
n = int(input())
for test in range(n):
    g = int(input())
    table = defaultdict(lambda : None)
    guests = list(map(int, input().split()))
    single = None
    for i in range(g):
        if table[guests[i]] == True:
            table[guests[i]] = False
        else:
            table[guests[i]] = True
    for k,v in table.items():
        if v == True:
            print("Case #" + str(test + 1) + ": " + str(k))
            break
