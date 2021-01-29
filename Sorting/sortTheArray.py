n = int(input())
a = list(map(int,input().split()))



s = list(a)
s.sort()

l = 0
r = 0
seg = 0
count = 0
for i in range(n):
    if (s[i] == a[i]):
        count += 1

if count == n:
    print("yes")
    print(1, 1)
else:
    for i in range(1,n):
        if (seg == 1):
            break
        #detect where the disrupt happens
        if (a[i-1] > a[i]):
            l = i-1
            r = i-1
            while (i < n and a[l] > a[i]):
                i += 1
                r += 1
            a[l:r+1] = a[l:r+1][::-1]
            seg += 1
        else:
            i += 1
    if (a == s):
        print("yes")
        print(l+1, r+1)
    else:
        print("no")
