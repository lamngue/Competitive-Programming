firstLine = input().split()
n = int(firstLine[0])
m = int(firstLine[1])
good = (list(map(int,input().split()))) #[1,2,3]
probs = (list(map(int,input().split()))) #[1,1,1,1,1]

#check how many problems are good
def check(good, probs):
    count = 0
    n = len(good)
    m = len(probs)
    j = 0
    while (j < m):
        if count < n and probs[j] >= good[count]:
            count += 1
        j += 1
    return count

def george(n,m,good,probs):
    return n - check(good,probs)
        
    

print(george(n,m,good,probs))
