line1 = input().split()
na = int(line1[0])
nb = int(line1[1])
line2 = input().split()
k = int(line2[0])
m = int(line2[1])
a = list(map(int,input().split()))
b = list(map(int,input().split()))


##partA = a[:k] #[
##partB = b[nb-m:] #[1,2,3,4,5,6]
##
##def check(partA, partB, k):
##    for i in range(k):
##        if (partA[i] >= partB[0]):
##            return False
##    return True 



if(a[k-1] < b[nb-m]):
    print("YES")
else:
    print("NO")

### every elements in A is smaller than B
##if (all(i < b[0] for i in a)):
##    # if all elements are the same or distinct
##    if (len(set(a)) == 1 or len(set(a)) == na):
##        print("YES")
### if two arrays are equal in size
##elif (na == nb):
##     # if all elements are the same
##    if (len(set(a)) == 1 and a[0] < b[0]):
##        print("YES")
##    elif (k < na and a[na-1] == b[0] and len(set(a)) > 1):
##        print("YES")
##    elif (k < na and a == b and len(set(a)) == len(set(b)) and len(set(a)) > 1):
##        print("YES")
##    else:
##        print("NO")
##elif (na < nb):
##    
##else:
##    print("NO")
