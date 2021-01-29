f = input().split()
n = int(f[0])
w = int(f[1])


cups = list(map(int,input().split()))

cups.sort()
# how much water for each boi
smaller = min(cups[0], cups[n]/2)
total = 3*smaller*n

if (total > w):
    print(w)
else:
    print(total)


