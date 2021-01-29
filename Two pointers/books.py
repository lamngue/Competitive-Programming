f = input().split()
n = int(f[0]) 
t = int(f[1]) #number of free minutes
books = list(map(int,input().split()))

count = 0
s = 0 #totalSoFar
start = 0 #startBook
for i in range(n):
    s += books[i]
    if (s <= t):
        count += 1
    else:
        #discard the starting book
        s -= books[start]
        start += 1
print(count)
